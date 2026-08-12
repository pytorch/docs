# Parameter

*class*torch.nn.parameter.Parameter(*data=None*, *requires_grad=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/nn/parameter.py#L30)

A kind of Tensor that is to be considered a module parameter.

Parameters are [`Tensor`](../tensors.html#torch.Tensor) subclasses, that have a
very special property when used with `Module` s - when they're
assigned as Module attributes they are automatically added to the list of
its parameters, and will appear e.g. in `parameters()` iterator.
Assigning a Tensor doesn't have such effect. This is because one might
want to cache some temporary state, like last hidden state of the RNN, in
the model. If there was no such class as `Parameter`, these
temporaries would get registered too.

Parameters:

- **data** ([*Tensor*](../tensors.html#torch.Tensor)) - parameter tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if the parameter requires gradient. Note that
the torch.no_grad() context does NOT affect the default behavior of
Parameter creation-the Parameter will still have requires_grad=True in
`no_grad` mode. See [Locally disabling gradient computation](../notes/autograd.html#locally-disable-grad-doc) for more
details. Default: True