# torch.autograd.Function.jvp

*static*Function.jvp(*ctx*, **grad_inputs*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/function.py#L536)

Define a formula for differentiating the operation with forward mode automatic differentiation.

This function is to be overridden by all subclasses.
It must accept a context `ctx` as the first argument, followed by
as many inputs as the [`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward) got (None will be passed in
for non tensor inputs of the forward function),
and it should return as many tensors as there were outputs to
[`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward). Each argument is the gradient w.r.t the given input,
and each returned value should be the gradient w.r.t. the
corresponding output. If an output is not a Tensor or the function is not
differentiable with respect to that output, you can just pass None as a
gradient for that input.

You can use the `ctx` object to pass any value from the forward to this
functions.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)