# torch.Tensor.storage

Tensor.storage() → [torch.TypedStorage](../storage.html#torch.TypedStorage)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/_tensor.py#L290)

Returns the underlying [`TypedStorage`](../storage.html#torch.TypedStorage).

Warning

[`TypedStorage`](../storage.html#torch.TypedStorage) is deprecated. It will be removed in the future, and
[`UntypedStorage`](../storage.html#torch.UntypedStorage) will be the only storage class. To access the
[`UntypedStorage`](../storage.html#torch.UntypedStorage) directly, use [`Tensor.untyped_storage()`](torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage).