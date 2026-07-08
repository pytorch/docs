# torch.Tensor.data_ptr

Tensor.data_ptr() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the address of the first element of `self` tensor.

Note

If the tensor is a copy-on-write tensor (e.g. created via
`_lazy_clone()`), calling this method will materialize the
copy. Use [`const_data_ptr()`](torch.Tensor.const_data_ptr.html#torch.Tensor.const_data_ptr) if you only need read-only access
to the data pointer.