# BackwardCFunction

*class*torch.autograd.function.BackwardCFunction[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L424)

This class is used for internal autograd work. Do not use.

apply(**args*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L440)

Apply method used when executing this Node during the backward.

Called by the autograd engine (non-boxed path) and by direct
grad_fn.apply() calls. When boxed_grads_call is True, boxes
grads into a mutable list before calling user's backward.

apply_boxed(**args*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L454)

Apply method called by the autograd engine when boxed_grads_call
is True. Grads arrive as a single mutable list argument, allowing
backward to free individual grads mid-execution.

apply_jvp(**args*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L462)

Apply method used when executing forward mode AD during the forward

*property*input_grad_buffers*: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None), ...]*

Return existing buffers for accumulating gradients of this Function's inputs.

Each entry corresponds to an argument passed to
`forward()`, in the same order.
Each entry is `None` or the autograd engine's current `InputBuffer` for
that input. A non-`None` buffer contains gradient contributions already
produced during the current backward. A custom backward may accumulate its
contribution directly into the buffer and return `None` for that input,
fusing gradient computation with accumulation and avoiding a separate
gradient tensor.

Availability follows backward execution order and is independent for each
input. An entry is `None` when no earlier producer has contributed to
that input, or when the existing buffer is aliased or cannot safely be
updated in place.

For example, `x` has another forward use while `weight` does not. The
custom backward conditionally fuses accumulation only for `grad_x`:

```
>>> class Matmul(torch.autograd.Function):
>>> @staticmethod
>>> def forward(ctx, x, weight):
>>> ctx.save_for_backward(x, weight)
>>> return x @ weight
>>>
>>> @staticmethod
>>> def backward(ctx, grad_output):
>>> x, weight = ctx.saved_tensors
>>> x_buffer, _ = ctx.input_grad_buffers
>>> if x_buffer is not None:
>>> # Computes grad_x and adds it to the existing buffer.
>>> matmul_backward_input_acc(
>>> grad_output, weight, acc_into=x_buffer
>>> )
>>> grad_x = None
>>> else:
>>> grad_x = matmul_backward_input(grad_output, weight)
>>> grad_weight = matmul_backward_weight(grad_output, x)
>>> return grad_x, grad_weight
>>>
>>> loss = Matmul.apply(x, weight).sum() + other_op(x).sum()
```

If `other_op` produces its contribution first, `x_buffer` can expose
that partial sum. If `Matmul` runs first, `x_buffer` is `None` and it
returns a separate tensor instead. The fallback lets the function work
under either ordering.

Warning

A returned buffer is valid only while the current custom `backward`
invocation is running. Mutate it synchronously and do not retain it.
A later producer may replace the engine's buffer, making a retained
tensor stale.

After receiving a non-`None` buffer, calling `backward` or
`grad` before the custom backward returns raises an error.

All engine-scheduled producers that use or subsequently update an
exposed buffer must execute on the same device, autograd engine thread,
and stream.

This property is available only while a Python custom `backward` is
executing during an eager, first-order [`backward()`](torch.Tensor.backward.html#torch.Tensor.backward),
[`torch.autograd.backward()`](torch.autograd.backward.html#torch.autograd.backward), or [`torch.autograd.grad()`](torch.autograd.grad.html#torch.autograd.grad) call. It is
unavailable with `create_graph=True`, anomaly detection, a post-hook on
the producing autograd node, or stale capture stream overrides.

Note

For a leaf input, a non-`None` entry exposes its execution-local
`InputBuffer`, not its existing `.grad`. All contributions are
first combined in that buffer. During `backward`, `AccumulateGrad`
then runs once with the completed buffer to update `.grad` and run
its usual hooks. [`torch.autograd.grad()`](torch.autograd.grad.html#torch.autograd.grad) instead returns the
completed buffer without updating `.grad`.

During `backward`, a custom backward that instead accumulates
directly into a leaf `.grad` and returns `None` does not use this
interface. It is responsible for managing `.grad` state, including
initialization and lifetime, synchronization with all other producers,
and any `AccumulateGrad` hook behavior bypassed by the direct write.

mark_dirty(**args*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L244)

Mark given tensors as modified in an in-place operation.

This should be called at most once, in either the `setup_context()`
or `forward()` methods, and all arguments should be inputs.

Every tensor that's been modified in-place in a call to `forward()`
should be given to this function, to ensure correctness of our checks.
It doesn't matter whether the function is called before or after
modification.

Examples::

```
>>> class Inplace(Function):
>>> @staticmethod
>>> def forward(ctx, x):
>>> x_npy = x.numpy() # x_npy shares storage with x
>>> x_npy += 1
>>> ctx.mark_dirty(x)
>>> return x
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, grad_output):
>>> return grad_output
>>>
>>> a = torch.tensor(1., requires_grad=True, dtype=torch.double).clone()
>>> b = a * a
>>> Inplace.apply(a) # This would lead to wrong gradients!
>>> # but the engine would not know unless we mark_dirty
>>> b.backward() # RuntimeError: one of the variables needed for gradient
>>> # computation has been modified by an inplace operation
```

mark_non_differentiable(**args*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L290)

Mark outputs as non-differentiable.

This should be called at most once, in either the `setup_context()`
or `forward()` methods, and all arguments should be tensor outputs.

This will mark outputs as not requiring gradients, increasing the
efficiency of backward computation. You still need to accept a gradient
for each output in `backward()`, but it's always going to
be a zero tensor with the same shape as the shape of a corresponding
output.

This is used e.g. for indices returned from a sort. See example::

```
>>> class Func(Function):
>>> @staticmethod
>>> def forward(ctx, x):
>>> sorted, idx = x.sort()
>>> ctx.mark_non_differentiable(idx)
>>> ctx.save_for_backward(x, idx)
>>> return sorted, idx
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, g1, g2): # still need to accept g2
>>> x, idx = ctx.saved_tensors
>>> grad_input = torch.zeros_like(x)
>>> grad_input.index_add_(0, idx, g1)
>>> return grad_input
```

save_for_backward(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L127)

Save given tensors for a future call to `backward()`.

`save_for_backward` should be called at most once, in either the
`setup_context()` or `forward()` methods, and only with tensors.

All tensors intended to be used in the backward pass should be saved
with `save_for_backward` (as opposed to directly on `ctx`) to prevent
incorrect gradients and memory leaks, and enable the application of saved
tensor hooks. See [`torch.autograd.graph.saved_tensors_hooks`](../autograd.html#torch.autograd.graph.saved_tensors_hooks).
See [Extending torch.autograd](../notes/extending.html#extending-autograd) for more details.

Note that if intermediary tensors, tensors that are neither inputs
nor outputs of `forward()`, are saved for backward, your custom Function
may not support double backward.
Custom Functions that do not support double backward should decorate their
`backward()` method with `@once_differentiable` so that performing
double backward raises an error. If you'd like to support double backward,
you can either recompute intermediaries based on the inputs during backward
or return the intermediaries as the outputs of the custom Function. See the
[double backward tutorial](https://pytorch.org/tutorials/intermediate/custom_function_double_backward_tutorial.html)
for more details.

In `backward()`, saved tensors can be accessed through the `saved_tensors`
attribute. Before returning them to the user, a check is made to ensure
they weren't used in any in-place operation that modified their content.

Arguments can also be `None`. This is a no-op.

See [Extending torch.autograd](../notes/extending.html#extending-autograd) for more details on how to use this method.

Example:

```
>>> class Func(Function):
>>> @staticmethod
>>> def forward(ctx, x: torch.Tensor, y: torch.Tensor, z: int):
>>> w = x * z
>>> out = x * y + y * z + w * y
>>> ctx.save_for_backward(x, y, w, out)
>>> ctx.z = z # z is not a tensor
>>> return out
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, grad_out):
>>> x, y, w, out = ctx.saved_tensors
>>> z = ctx.z
>>> gx = grad_out * (y + y * z)
>>> gy = grad_out * (x + z + w)
>>> gz = None
>>> return gx, gy, gz
>>>
>>> a = torch.tensor(1., requires_grad=True, dtype=torch.double)
>>> b = torch.tensor(2., requires_grad=True, dtype=torch.double)
>>> c = 4
>>> d = Func.apply(a, b, c)
```

save_for_forward(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L188)

Save given tensors for a future call to `jvp()`.

`save_for_forward` should be called at most once, in either the
`setup_context()` or `forward()` methods, and all arguments
should be tensors.

In `jvp()`, saved objects can be accessed through the `saved_tensors`
attribute.

Arguments can also be `None`. This is a no-op.

See [Extending torch.autograd](../notes/extending.html#extending-autograd) for more details on how to use this method.

Example:

```
>>> class Func(torch.autograd.Function):
>>> @staticmethod
>>> def forward(ctx, x: torch.Tensor, y: torch.Tensor, z: int):
>>> ctx.save_for_backward(x, y)
>>> ctx.save_for_forward(x, y)
>>> ctx.z = z
>>> return x * y * z
>>>
>>> @staticmethod
>>> def jvp(ctx, x_t, y_t, _):
>>> x, y = ctx.saved_tensors
>>> z = ctx.z
>>> return z * (y * x_t + x * y_t)
>>>
>>> @staticmethod
>>> def vjp(ctx, grad_out):
>>> x, y = ctx.saved_tensors
>>> z = ctx.z
>>> return z * grad_out * y, z * grad_out * x, None
>>>
>>> a = torch.tensor(1., requires_grad=True, dtype=torch.double)
>>> t = torch.tensor(1., dtype=torch.double)
>>> b = torch.tensor(2., requires_grad=True, dtype=torch.double)
>>> c = 4
>>>
>>> with fwAD.dual_level():
>>> a_dual = fwAD.make_dual(a, t)
>>> d = Func.apply(a_dual, b, c)
```

set_materialize_grads(*value*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L362)

Set whether to materialize grad tensors. Default is `True`.

This should be called only from either the `setup_context()` or
`forward()` methods.

If `True`, undefined grad tensors will be expanded to tensors full of zeros
prior to calling the `backward()` and `jvp()` methods.

Example:

```
>>> class SimpleFunc(Function):
>>> @staticmethod
>>> def forward(ctx, x):
>>> return x.clone(), x.clone()
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, g1, g2):
>>> return g1 + g2 # No check for None necessary
>>>
>>> # We modify SimpleFunc to handle non-materialized grad outputs
>>> class Func(Function):
>>> @staticmethod
>>> def forward(ctx, x):
>>> ctx.set_materialize_grads(False)
>>> ctx.save_for_backward(x)
>>> return x.clone(), x.clone()
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, g1, g2):
>>> x, = ctx.saved_tensors
>>> grad_input = torch.zeros_like(x)
>>> if g1 is not None: # We must check for None now
>>> grad_input += g1
>>> if g2 is not None:
>>> grad_input += g2
>>> return grad_input
>>>
>>> a = torch.tensor(1., requires_grad=True)
>>> b, _ = Func.apply(a) # induces g2 to be undefined
```

set_output_grad_dtype(**dtypes*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/function.py#L322)

Declare the gradient dtype for each of this Function's outputs.

This should be called at most once, from either the
`setup_context()` or `forward()` methods. The number of
declarations must match the number of returned values, and each argument
corresponds positionally to the output at the same index.

For each output, pass the dtype your backward should receive its
gradient in:

- Pass a [`torch.dtype`](../tensor_attributes.html#torch.dtype) and the engine guarantees the gradient
handed to backward has that dtype. This is only valid for a
differentiable Tensor output.
- Pass `None` and the gradient is handed to backward with whatever
dtype it already has. This is also the only valid choice for a
non-Tensor or non-differentiable output, which has no gradient.
- Omit this call (or pass the output's own dtype) and the gradient is
handed to backward in the output's dtype, which is the default.

For example:

```
>>> @staticmethod
>>> def forward(ctx, x):
>>> t1 = x.sin()
>>> t2 = x.cos()
>>> t3 = x.tan()
>>> ctx.set_output_grad_dtype(torch.float32, t2.dtype, None, None)
>>> return t1, t2, t3, "not a tensor"
```

This ensures that backward receives `t1`'s gradient in `float32`,
keeps the default behavior for `t2`'s gradient via `t2.dtype`,
passes `t3`'s gradient through uncast with `None`, and uses `None`
as the placeholder for the trailing non-Tensor output.