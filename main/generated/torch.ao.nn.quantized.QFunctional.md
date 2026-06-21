# QFunctional

*class*torch.ao.nn.quantized.QFunctional[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/ao/nn/quantized/modules/functional_modules.py#L164)

Wrapper class for quantized operations.

The instance of this class can be used instead of the
`torch.ops.quantized` prefix. See example usage below.

Note

This class does not provide a `forward` hook. Instead, you must use
one of the underlying functions (e.g. `add`).

Examples:

```
>>> q_add = QFunctional()
>>> a = torch.quantize_per_tensor(torch.tensor(3.0), 1.0, 0, torch.qint32)
>>> b = torch.quantize_per_tensor(torch.tensor(4.0), 1.0, 0, torch.qint32)
>>> q_add.add(a, b) # Equivalent to ``torch.ops.quantized.add(a, b, 1.0, 0)``
```

Valid operation names:

- add
- cat
- mul
- add_relu
- add_scalar
- mul_scalar