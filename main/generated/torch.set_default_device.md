# torch.set_default_device

torch.set_default_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/__init__.py#L1617)

Sets the default `torch.Tensor` to be allocated on `device`. This
does not affect factory function calls which are called with an explicit
`device` argument. Factory calls will be performed as if they
were passed `device` as an argument.

To only temporarily change the default device instead of setting it
globally, use `with torch.device(device):` instead.

The default device is initially `cpu`. If you set the default tensor
device to another device (e.g., `cuda`) without a device index, tensors
will be allocated on whatever the current device for the device type,
even after [`torch.cuda.set_device()`](torch.cuda.set_device.html#torch.cuda.set_device) is called.

Warning

This function imposes a slight performance cost on every Python
call to the torch API (not just factory functions). If this
is causing problems for you, please comment on
[pytorch/pytorch#92701](https://github.com/pytorch/pytorch/issues/92701)

Note

This doesn't affect functions that create tensors that share the same memory as the input, like:
[`torch.from_numpy()`](torch.from_numpy.html#torch.from_numpy) and [`torch.frombuffer()`](torch.frombuffer.html#torch.frombuffer)

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, or None) - the device to set as
default, or `None` to clear the override. An integer is
interpreted as an index for the current accelerator.

Example:

```
>>> torch.get_default_device()
device(type='cpu')
>>> torch.set_default_device('cuda') # current device is 0
>>> torch.get_default_device()
device(type='cuda', index=0)
>>> torch.set_default_device('cuda')
>>> torch.cuda.set_device('cuda:1') # current device is 1
>>> torch.get_default_device()
device(type='cuda', index=1)
>>> torch.set_default_device('cuda:1')
>>> torch.get_default_device()
device(type='cuda', index=1)
```