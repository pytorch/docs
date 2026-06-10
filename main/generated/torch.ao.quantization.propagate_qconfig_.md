# propagate_qconfig

*class*torch.ao.quantization.propagate_qconfig_(*module*, *qconfig_dict=None*, *prepare_custom_config_dict=None*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/quantization/quantize.py#L125)

Propagate qconfig through the module hierarchy and assign qconfig
attribute on each leaf module

Parameters:

- **module** - input module
- **qconfig_dict** - dictionary that maps from name or type of submodule to
quantization configuration, qconfig applies to all submodules of a
given module unless qconfig for the submodules are specified (when
the submodule already has qconfig attribute)
- **prepare_custom_config_dict** - dictionary for custom handling of modules
see docs for `prepare_fx()`

Returns:

None, module is modified inplace with qconfig attached