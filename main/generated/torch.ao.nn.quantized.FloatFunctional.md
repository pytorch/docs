# FloatFunctional

*class*torch.ao.nn.quantized.FloatFunctional[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/ao/nn/quantized/modules/functional_modules.py#L11)

State collector class for float operations.

The instance of this class can be used instead of the `torch.` prefix for
some operations. See example usage below.

Note

This class does not provide a `forward` hook. Instead, you must use
one of the underlying functions (e.g. `add`).

Examples:

```
>>> f_add = FloatFunctional()
>>> a = torch.tensor(3.0)
>>> b = torch.tensor(4.0)
>>> f_add.add(a, b) # Equivalent to ``torch.add(a, b)``
```

Valid operation names:

- add
- cat
- mul
- add_relu
- add_scalar
- mul_scalar