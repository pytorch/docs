# get_custom_module_class_keys

*class*torch.ao.quantization.fx.utils.get_custom_module_class_keys(*custom_module_mapping*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/ao/quantization/fx/utils.py#L118)

Get all the unique custom module keys in the custom config dict.

Example input:

```
{
 QuantType.STATIC: {CustomModule1: ObservedCustomModule},
 QuantType.DYNAMIC: {CustomModule2: DynamicObservedCustomModule},
 QuantType.WEIGHT_ONLY: {CustomModule3: WeightOnlyObservedCustomModule},
}
```

Example output:

```
# extract the keys across all inner STATIC, DYNAMIC, and WEIGHT_ONLY dicts
[CustomModule1, CustomModule2, CustomModule3]
```

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]