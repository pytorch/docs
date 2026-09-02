# UninitializedParameter

*class*torch.nn.parameter.UninitializedParameter(*requires_grad=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/nn/parameter.py#L204)

A parameter that is not initialized.

Uninitialized Parameters are a special case of `torch.nn.Parameter`
where the shape of the data is still unknown.

Unlike a `torch.nn.Parameter`, uninitialized parameters
hold no data and attempting to access some properties, like their shape,
will throw a runtime error. The only operations that can be performed on an uninitialized
parameter are changing its datatype, moving it to a different device and
converting it to a regular `torch.nn.Parameter`.

The default device or dtype to use when the parameter is materialized can be set
during construction using e.g. `device='cuda'`.

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/nn/parameter.py#L30)

alias of [`Parameter`](torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter)