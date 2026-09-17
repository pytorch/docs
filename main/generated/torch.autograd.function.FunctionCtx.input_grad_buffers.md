# torch.autograd.function.FunctionCtx.input_grad_buffers

*property*FunctionCtx.input_grad_buffers*: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None), ...]*

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