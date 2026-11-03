# torch.is_storage

torch.is_storage(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/fbab7cc90f5699714d5785aaa2f153c739435d6f/torch/__init__.py#L1562)

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