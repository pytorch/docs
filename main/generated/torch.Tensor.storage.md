# torch.Tensor.storage

Tensor.storage() → [torch.TypedStorage](../storage.html#torch.TypedStorage)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/_tensor.py#L290)

Returns the underlying [`TypedStorage`](../storage.html#torch.TypedStorage).

Warning

[`TypedStorage`](../storage.html#torch.TypedStorage) is deprecated. It will be removed in the future, and
[`UntypedStorage`](../storage.html#torch.UntypedStorage) will be the only storage class. To access the
[`UntypedStorage`](../storage.html#torch.UntypedStorage) directly, use [`Tensor.untyped_storage()`](torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage).