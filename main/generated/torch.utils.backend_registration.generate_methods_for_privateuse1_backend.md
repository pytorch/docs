# torch.utils.backend_registration.generate_methods_for_privateuse1_backend

torch.utils.backend_registration.generate_methods_for_privateuse1_backend(*for_tensor=True*, *for_module=True*, *for_packed_sequence=True*, *for_storage=False*, *unsupported_dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/utils/backend_registration.py#L381)

Automatically generate attributes and methods for the custom backend after rename privateuse1 backend.

In the default scenario, storage-related methods will not be generated automatically.

When you implement kernels for various torch operations, and register them to the PrivateUse1 dispatch key.
And call the function torch.rename_privateuse1_backend("foo") to rename your backend name.
At this point, you can easily register specific methods and attributes by calling this function.
Just like torch.Tensor.foo(), torch.Tensor.is_foo, torch.Storage.foo(), torch.Storage.is_foo.

Note: We recommend you use generic functions (check devices are equal or to(device=)).
We provide these methods for convenience only and they will be "monkey patched" onto the objects
and so will not be properly typed. For Storage methods generate, if you need to support sparse data storage,
you need to extend the implementation yourself.

Parameters:

- **for_tensor** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether register related methods for torch.Tensor class.
- **for_module** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether register related methods for torch.nn.Module class.
- **for_storage** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether register related methods for torch.Storage class.
- **unsupported_dtype** (*List**[*[*torch.dtype*](../tensor_attributes.html#torch.dtype)*]*) - takes effect only when the storage method needs to be generated,
indicating that the storage does not support the torch.dtype type.

Example:

```
>>> torch.utils.rename_privateuse1_backend("foo")
>>> torch.utils.generate_methods_for_privateuse1_backend()
# Then automatically generate backend-related attributes and methods.
>>> a = torch.tensor(2).foo()
>>> a.is_foo
>>> hasattr(torch.nn.Module, 'foo')
```