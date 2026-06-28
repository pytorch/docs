# UninitializedBuffer

*class*torch.nn.parameter.UninitializedBuffer(*requires_grad=False*, *device=None*, *dtype=None*, *persistent=True*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/parameter.py#L281)

A buffer that is not initialized.

Uninitialized Buffer is a special case of [`torch.Tensor`](../tensors.html#torch.Tensor)
where the shape of the data is still unknown.

Unlike a [`torch.Tensor`](../tensors.html#torch.Tensor), uninitialized parameters
hold no data and attempting to access some properties, like their shape,
will throw a runtime error. The only operations that can be performed on an uninitialized
parameter are changing its datatype, moving it to a different device and
converting it to a regular [`torch.Tensor`](../tensors.html#torch.Tensor).

The default device or dtype to use when the buffer is materialized can be set
during construction using e.g. `device='cuda'`.