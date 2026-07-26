# torch.Tensor.storage

Tensor.storage() → [torch.TypedStorage](../storage.html#torch.TypedStorage)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/_tensor.py#L290)

Returns the underlying [`TypedStorage`](../storage.html#torch.TypedStorage).

Warning

[`TypedStorage`](../storage.html#torch.TypedStorage) is deprecated. It will be removed in the future, and
[`UntypedStorage`](../storage.html#torch.UntypedStorage) will be the only storage class. To access the
[`UntypedStorage`](../storage.html#torch.UntypedStorage) directly, use [`Tensor.untyped_storage()`](torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage).