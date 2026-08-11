# torch.is_storage

torch.is_storage(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/__init__.py#L1541)

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