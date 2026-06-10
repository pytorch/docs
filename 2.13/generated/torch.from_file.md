# torch.from_file

torch.from_file(*filename*, *shared=None*, *size=0*, ***, *dtype=None*, *layout=None*, *device=None*, *pin_memory=False*)

Creates a CPU tensor with a storage backed by a memory-mapped file.

If `shared` is True, then memory is shared between processes. All changes are written to the file.
If `shared` is False, then changes to the tensor do not affect the file.

`size` is the number of elements in the Tensor. If `shared` is `False`, then the file must contain
at least `size * sizeof(dtype)` bytes. If `shared` is `True` the file will be created if needed.

Note

Only CPU tensors can be mapped to files.

Note

For now, tensors with storages backed by a memory-mapped file cannot be created in pinned memory.

Parameters:

- **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - file name to map
- **shared** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the
underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html))
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of elements in the tensor

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> t = torch.randn(2, 5, dtype=torch.float64)
>>> t.numpy().tofile('storage.pt')
>>> t_mapped = torch.from_file('storage.pt', shared=False, size=10, dtype=torch.float64)
```