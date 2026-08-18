# get_custom_module_class_keys

*class*torch.ao.quantization.fx.utils.get_custom_module_class_keys(*custom_module_mapping*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/ao/quantization/fx/utils.py#L118)

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