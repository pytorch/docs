# torch.is_storage

torch.is_storage(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/__init__.py#L1176)

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