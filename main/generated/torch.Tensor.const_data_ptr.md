# torch.Tensor.const_data_ptr

Tensor.const_data_ptr() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the address of the first element of `self` tensor.

Unlike [`data_ptr()`](torch.Tensor.data_ptr.html#torch.Tensor.data_ptr), this is guaranteed to be a read-only access
that will not trigger copy-on-write materialization. For regular
(non-COW) tensors, the return value is identical to [`data_ptr()`](torch.Tensor.data_ptr.html#torch.Tensor.data_ptr).

Warning

The returned pointer must not be used to mutate the tensor data.
Use [`data_ptr()`](torch.Tensor.data_ptr.html#torch.Tensor.data_ptr) when write access is needed.