# torch.is_storage

torch.is_storage(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/4581144c216b65e4e1b5c6eea26d4212239a231d/torch/__init__.py#L1575)

Returns True if obj is a PyTorch storage object.

Parameters:

**obj** (*Object*) - Object to test

Return type:

[*TypeGuard*](https://docs.python.org/3/library/typing.html#typing.TypeGuard)[[*TypedStorage*](../storage.html#torch.TypedStorage) | [*UntypedStorage*](../storage.html#torch.UntypedStorage)]

Example:

```
>>> import torch
>>> # UntypedStorage (recommended)
>>> tensor = torch.tensor([1, 2, 3])
>>> storage = tensor.untyped_storage()
>>> torch.is_storage(storage)
True
>>>
>>> # TypedStorage (legacy)
>>> typed_storage = torch.TypedStorage(5, dtype=torch.float32)
>>> torch.is_storage(typed_storage)
True
>>>
>>> # regular tensor (should return False)
>>> torch.is_storage(tensor)
False
>>>
>>> # non-storage object
>>> torch.is_storage([1, 2, 3])
False
```