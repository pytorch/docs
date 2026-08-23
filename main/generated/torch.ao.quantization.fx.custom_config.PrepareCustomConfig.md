# PrepareCustomConfig

*class*torch.ao.quantization.fx.custom_config.PrepareCustomConfig[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L46)

Custom configuration for [`prepare_fx()`](torch.ao.quantization.quantize_fx.prepare_fx.html#torch.ao.quantization.quantize_fx.prepare_fx) and
[`prepare_qat_fx()`](torch.ao.quantization.quantize_fx.prepare_qat_fx.html#torch.ao.quantization.quantize_fx.prepare_qat_fx).

Example usage:

```
prepare_custom_config = PrepareCustomConfig() .set_standalone_module_name("module1", qconfig_mapping, example_inputs, child_prepare_custom_config, backend_config) .set_standalone_module_class(MyStandaloneModule, qconfig_mapping, example_inputs, child_prepare_custom_config, backend_config) .set_float_to_observed_mapping(FloatCustomModule, ObservedCustomModule) .set_non_traceable_module_names(["module2", "module3"]) .set_non_traceable_module_classes([NonTraceableModule1, NonTraceableModule2]) .set_input_quantized_indexes([0]) .set_output_quantized_indexes([0]) .set_preserved_attributes(["attr1", "attr2"])
```

*classmethod*from_dict(*prepare_custom_config_dict*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L184)

Create a `PrepareCustomConfig` from a dictionary with the following items:

> "standalone_module_name": a list of (module_name, qconfig_mapping, example_inputs,
> child_prepare_custom_config, backend_config) tuples
> 
> 
> 
> 
> "standalone_module_class" a list of (module_class, qconfig_mapping, example_inputs,
> child_prepare_custom_config, backend_config) tuples
> 
> 
> 
> 
> "float_to_observed_custom_module_class": a nested dictionary mapping from quantization
> mode to an inner mapping from float module classes to observed module classes, e.g.
> {"static": {FloatCustomModule: ObservedCustomModule}}
> 
> 
> 
> 
> "non_traceable_module_name": a list of modules names that are not symbolically traceable
> "non_traceable_module_class": a list of module classes that are not symbolically traceable
> "input_quantized_idxs": a list of indexes of graph inputs that should be quantized
> "output_quantized_idxs": a list of indexes of graph outputs that should be quantized
> "preserved_attributes": a list of attributes that persist even if they are not used in `forward`

This function is primarily for backward compatibility and may be removed in the future.

Return type:

*PrepareCustomConfig*

set_float_to_observed_mapping(*float_class*, *observed_class*, *quant_type=QuantType.STATIC*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L120)

Set the mapping from a custom float module class to a custom observed module class.

The observed module class must have a `from_float` class method that converts the float module class
to the observed module class. This is currently only supported for static quantization.

Return type:

*PrepareCustomConfig*

set_input_quantized_indexes(*indexes*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L159)

Set the indexes of the inputs of the graph that should be quantized.
Inputs are otherwise assumed to be in fp32 by default instead.

Return type:

*PrepareCustomConfig*

set_non_traceable_module_classes(*module_classes*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L150)

Set the modules that are not symbolically traceable, identified by class.

Return type:

*PrepareCustomConfig*

set_non_traceable_module_names(*module_names*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L141)

Set the modules that are not symbolically traceable, identified by name.

Return type:

*PrepareCustomConfig*

set_output_quantized_indexes(*indexes*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L167)

Set the indexes of the outputs of the graph that should be quantized.
Outputs are otherwise assumed to be in fp32 by default instead.

Return type:

*PrepareCustomConfig*

set_preserved_attributes(*attributes*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L175)

Set the names of the attributes that will persist in the graph module even if they are not used in
the model's `forward` method.

Return type:

*PrepareCustomConfig*

set_standalone_module_class(*module_class*, *qconfig_mapping*, *example_inputs*, *prepare_custom_config*, *backend_config*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L100)

Set the configuration for running a standalone module identified by `module_class`.

If `qconfig_mapping` is None, the parent `qconfig_mapping` will be used instead.
If `prepare_custom_config` is None, an empty `PrepareCustomConfig` will be used.
If `backend_config` is None, the parent `backend_config` will be used instead.

Return type:

*PrepareCustomConfig*

set_standalone_module_name(*module_name*, *qconfig_mapping*, *example_inputs*, *prepare_custom_config*, *backend_config*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L80)

Set the configuration for running a standalone module identified by `module_name`.

If `qconfig_mapping` is None, the parent `qconfig_mapping` will be used instead.
If `prepare_custom_config` is None, an empty `PrepareCustomConfig` will be used.
If `backend_config` is None, the parent `backend_config` will be used instead.

Return type:

*PrepareCustomConfig*

to_dict()[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/quantization/fx/custom_config.py#L320)

Convert this `PrepareCustomConfig` to a dictionary with the items described in
`from_dict()`.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]