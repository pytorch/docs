# torch.Tensor.storage

Tensor.storage() → [torch.TypedStorage](../storage.html#torch.TypedStorage)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/_tensor.py#L291)

Returns the underlying [`TypedStorage`](../storage.html#torch.TypedStorage).

Warning

[`TypedStorage`](../storage.html#torch.TypedStorage) is deprecated. It will be removed in the future, and
[`UntypedStorage`](../storage.html#torch.UntypedStorage) will be the only storage class. To access the
[`UntypedStorage`](../storage.html#torch.UntypedStorage) directly, use [`Tensor.untyped_storage()`](torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage).