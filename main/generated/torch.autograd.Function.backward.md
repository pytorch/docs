# torch.autograd.Function.backward

*static*Function.backward(*ctx*, **grad_outputs*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/autograd/function.py#L432)

Define a formula for differentiating the operation with backward mode automatic differentiation.

This function is to be overridden by all subclasses.
(Defining this function is equivalent to defining the `vjp` function.)

It must accept a context `ctx` as the first argument, followed by
as many outputs as the [`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward) returned (None will be passed in
for non tensor outputs of the forward function),
and it should return as many tensors, as there were inputs to
[`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward). Each argument is the gradient w.r.t the given output,
and each returned value should be the gradient w.r.t. the
corresponding input. If an input is not a Tensor or is a Tensor not
requiring grads, you can just pass None as a gradient for that input.

The context can be used to retrieve tensors saved during the forward
pass. It also has an attribute `ctx.needs_input_grad` as a tuple
of booleans representing whether each input needs gradient. E.g.,
[`backward()`](torch.autograd.backward.html#torch.autograd.backward) will have `ctx.needs_input_grad[0] = True` if the
first input to [`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward) needs gradient computed w.r.t. the
output.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)