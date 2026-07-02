# AffineQuantizedObserverBase

*class*torch.ao.quantization.observer.AffineQuantizedObserverBase(*mapping_type*, *target_dtype*, *granularity*, *quant_min=None*, *quant_max=None*, *eps=None*, *scale_dtype=None*, *zero_point_dtype=None*, *preserve_zero=True*, *zero_point_domain=ZeroPointDomain.INT*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/quantization/observer.py#L1824)

Observer module for affine quantization ([pytorch/ao](https://github.com/pytorch/ao/tree/main/torchao/quantization#affine-quantization))

Parameters:

- **block_size** (*granularity and*) - The granularity of the quantization,
must specify at least one, if both are specified block_size takes precedence
Current supported granularity type are PerTensor and PerAxis
- **args** (*other*) - please see :class:torchao.dtypes.AffineQuantizedTensor

*abstract*calculate_qparams()[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/quantization/observer.py#L1874)

Calculate quantization parameter based on the stats attached to the observer module
and returns a tuple of scale and zero_point Tensor

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor)]

convert(*model*, *observer_node*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/quantization/observer.py#L1880)

Converts the observer node in the graph into its quantized representation

Parameters:

- **model** ([*GraphModule*](../fx.html#torch.fx.GraphModule)) - graph module to convert the observer node in
- **observer_node** ([*Node*](../fx.html#torch.fx.Node)) - the observer node to convert

*abstract*forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/quantization/observer.py#L1868)

forward function should take the input tensor
and updates internal stats and return the original input Tensor

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

*classmethod*with_args(***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/quantization/observer.py#L102)

Wrapper that allows creation of class factories.

This can be useful when there is a need to create classes with the same
constructor arguments, but different instances. Can be used in conjunction with
_callable_args

Example:

```
>>> Foo.with_args = classmethod(_with_args)
>>> foo_builder = Foo.with_args(a=3, b=4).with_args(answer=42)
>>> foo_instance1 = foo_builder()
>>> foo_instance2 = foo_builder()
>>> id(foo_instance1) == id(foo_instance2)
False
```