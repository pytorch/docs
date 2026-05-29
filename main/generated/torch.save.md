# torch.save

torch.save(*obj*, *f*, *pickle_module=pickle*, *pickle_protocol=2*, *_use_new_zipfile_serialization=True*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/serialization.py#L944)

Saves an object to a disk file.

See also: [Saving and loading tensors](../notes/serialization.html#saving-loading-tensors)

See [Layout Control](../notes/serialization.html#layout-control) for more advanced tools to manipulate a checkpoint.

Parameters:

- **obj** ([*object*](https://docs.python.org/3/library/functions.html#object)) - saved object
- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|*[*IO*](https://docs.python.org/3/library/typing.html#typing.IO)*[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - a file-like object (has to implement write and flush) or a string or
os.PathLike object containing a file name
- **pickle_module** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) - module used for pickling metadata and objects
- **pickle_protocol** ([*int*](https://docs.python.org/3/library/functions.html#int)) - can be specified to override the default protocol

Note

A common PyTorch convention is to save tensors using .pt file extension.

Note

PyTorch preserves storage sharing across serialization. See
[Saving and loading tensors preserves views](../notes/serialization.html#preserve-storage-sharing) for more details.

Note

The 1.6 release of PyTorch switched `torch.save` to use a new
zipfile-based file format. `torch.load` still retains the ability to
load files in the old format. If for any reason you want `torch.save`
to use the old format, pass the kwarg `_use_new_zipfile_serialization=False`.

Example

```
>>> # Save to file
>>> x = torch.tensor([0, 1, 2, 3, 4])
>>> torch.save(x, "tensor.pt")
>>> # Save to io.BytesIO buffer
>>> buffer = io.BytesIO()
>>> torch.save(x, buffer)
```