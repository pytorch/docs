# propagate_qconfig

*class*torch.ao.quantization.propagate_qconfig_(*module*, *qconfig_dict=None*, *prepare_custom_config_dict=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/ao/quantization/quantize.py#L125)

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