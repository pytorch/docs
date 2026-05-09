# FuseCustomConfig

*class*torch.ao.quantization.fx.custom_config.FuseCustomConfig[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/ao/quantization/fx/custom_config.py#L471)

Custom configuration for [`fuse_fx()`](torch.ao.quantization.quantize_fx.fuse_fx.html#torch.ao.quantization.quantize_fx.fuse_fx).

Example usage:

```
fuse_custom_config = FuseCustomConfig().set_preserved_attributes(
 ["attr1", "attr2"]
)
```

*classmethod*from_dict(*fuse_custom_config_dict*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/ao/quantization/fx/custom_config.py#L498)

Create a `ConvertCustomConfig` from a dictionary with the following items:

> "preserved_attributes": a list of attributes that persist even if they are not used in `forward`

This function is primarily for backward compatibility and may be removed in the future.

Return type:

*FuseCustomConfig*

set_preserved_attributes(*attributes*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/ao/quantization/fx/custom_config.py#L489)

Set the names of the attributes that will persist in the graph module even if they are not used in
the model's `forward` method.

Return type:

*FuseCustomConfig*

to_dict()[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/ao/quantization/fx/custom_config.py#L513)

Convert this `FuseCustomConfig` to a dictionary with the items described in
[`from_dict()`](torch.ao.quantization.fx.custom_config.ConvertCustomConfig.html#torch.ao.quantization.fx.custom_config.ConvertCustomConfig.from_dict).

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]