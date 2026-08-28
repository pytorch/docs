# torch.cuda.jiterator._create_multi_output_jit_fn

torch.cuda.jiterator._create_multi_output_jit_fn(*code_string*, *num_outputs*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/cuda/jiterator.py#L164)

Create a jiterator-generated cuda kernel for an elementwise op that supports returning one or more outputs.

Parameters:

- **code_string** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - CUDA code string to be compiled by jiterator. The entry functor must return value by reference.
- **num_outputs** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of outputs return by the kernel
- **kwargs** (*Dict**,**optional*) - Keyword arguments for generated function

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)

Example:

```
code_string = "template <typename T> void my_kernel(T x, T y, T alpha, T& out) { out = -x + alpha * y; }"
jitted_fn = create_jit_fn(code_string, alpha=1.0)
a = torch.rand(3, device="cuda")
b = torch.rand(3, device="cuda")
# invoke jitted function like a regular python function
result = jitted_fn(a, b, alpha=3.14)
```

Warning

This API is in beta and may change in future releases.

Warning

This API only supports up to 8 inputs and 8 outputs