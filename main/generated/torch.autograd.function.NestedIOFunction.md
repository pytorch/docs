# NestedIOFunction

*class*torch.autograd.function.NestedIOFunction(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L940)

This class is here only for backward compatibility reasons.
Use [`Function`](../autograd.html#torch.autograd.Function) instead of this for any new use case.

backward(**gradients*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L964)

Shared backward utility.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

backward_extended(**grad_output*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L1017)

User defined backward.

forward(**args*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L974)

Shared forward utility.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

forward_extended(**input*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L1011)

User defined forward.

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

*static*jvp(*ctx*, **grad_inputs*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L622)

Define a formula for differentiating the operation with forward mode automatic differentiation.

This function is to be overridden by all subclasses.
It must accept a context `ctx` as the first argument, followed by
as many inputs as the `forward()` got (None will be passed in
for non tensor inputs of the forward function),
and it should return as many tensors as there were outputs to
`forward()`. Each argument is the gradient w.r.t the given input,
and each returned value should be the gradient w.r.t. the
corresponding output. If an output is not a Tensor or the function is not
differentiable with respect to that output, you can just pass None as a
gradient for that input.

You can use the `ctx` object to pass any value from the forward to this
functions.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

mark_dirty(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L999)

See `Function.mark_dirty()`.

mark_non_differentiable(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L1005)

See `Function.mark_non_differentiable()`.

save_for_backward(**args*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L984)

See `Function.save_for_backward()`.

save_for_forward(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L188)

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

*property*saved_tensors

See `Function.saved_tensors()`.

set_materialize_grads(*value*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L362)

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

set_output_grad_dtype(**dtypes*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L322)

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

*static*setup_context(*ctx*, *inputs*, *output*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L542)

There are two ways to define the forward pass of an autograd.Function.

Either:

1. Override forward with the signature `forward(ctx, *args, **kwargs)`.
`setup_context` is not overridden. Setting up the ctx for backward
happens inside the `forward`.
2. Override forward with the signature `forward(*args, **kwargs)` and
override `setup_context`. Setting up the ctx for backward happens
inside `setup_context` (as opposed to inside the `forward`)

See [`torch.autograd.Function.forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward) and [Extending torch.autograd](../notes/extending.html#extending-autograd) for more details.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

*static*vjp(*ctx*, **grad_outputs*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L559)

Define a formula for differentiating the operation with backward mode automatic differentiation.

This function is to be overridden by all subclasses.
(Defining this function is equivalent to defining the `vjp` function.)

It must accept a context `ctx` as the first argument, followed by
as many outputs as the `forward()` returned (None will be passed in
for non tensor outputs of the forward function),
and it should return as many tensors, as there were inputs to
`forward()`. Each argument is the gradient w.r.t the given output,
and each returned value should be the gradient w.r.t. the
corresponding input. If an input is not a Tensor or is a Tensor not
requiring grads, you can just pass None as a gradient for that input.

The strides of the gradients passed to `backward()` are undefined:
they are not guaranteed to be contiguous or to match the strides of the
corresponding forward outputs, so implementations must not assume a
particular memory layout.

The context can be used to retrieve tensors saved during the forward
pass. It also has an attribute `ctx.needs_input_grad` as a tuple
of booleans representing whether each input needs gradient. E.g.,
`backward()` will have `ctx.needs_input_grad[0] = True` if the
first input to `forward()` needs gradient computed w.r.t. the
output.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

*static*vmap(*info*, *in_dims*, **args*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/autograd/function.py#L708)

Define the behavior for this autograd.Function underneath [`torch.vmap()`](torch.vmap.html#torch.vmap).

For a [`torch.autograd.Function()`](../autograd.html#torch.autograd.Function) to support
[`torch.vmap()`](torch.vmap.html#torch.vmap), you must either override this static method, or set
`generate_vmap_rule` to `True` (you may not do both).

If you choose to override this staticmethod: it must accept

- an `info` object as the first argument. `info.batch_size`
specifies the size of the dimension being vmapped over,
while `info.randomness` is the randomness option passed to
[`torch.vmap()`](torch.vmap.html#torch.vmap).
- an `in_dims` tuple as the second argument.
For each arg in `args`, `in_dims` has a corresponding
`Optional[int]`. It is `None` if the arg is not a Tensor or if
the arg is not being vmapped over, otherwise, it is an integer
specifying what dimension of the Tensor is being vmapped over.
- `*args`, which is the same as the args to `forward()`.

The return of the vmap staticmethod is a tuple of `(output, out_dims)`.
Similar to `in_dims`, `out_dims` should be of the same structure as
`output` and contain one `out_dim` per output that specifies if the
output has the vmapped dimension and what index it is in.

Please see [Extending torch.func with autograd.Function](../notes/extending.func.html#func-autograd-function) for more details.