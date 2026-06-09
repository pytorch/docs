# prepare

*class*torch.ao.quantization.prepare(*model*, *inplace=False*, *allow_list=None*, *observer_non_leaf_module_list=None*, *prepare_custom_config_dict=None*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/ao/quantization/quantize.py#L343)

Prepares a copy of the model for quantization calibration or quantization-aware training.

Quantization configuration should be assigned preemptively
to individual submodules in .qconfig attribute.

The model will be attached with observer or fake quant modules, and qconfig
will be propagated.

Parameters:

- **model** - input model to be modified in-place
- **inplace** - carry out model transformations in-place, the original module is mutated
- **allow_list** - list of quantizable modules
- **observer_non_leaf_module_list** - list of non-leaf modules we want to add observer
- **prepare_custom_config_dict** - customization configuration dictionary for prepare function

```
# Example of prepare_custom_config_dict:
prepare_custom_config_dict = {
 # user will manually define the corresponding observed
 # module class which has a from_float class method that converts
 # float custom module to observed custom module
 "float_to_observed_custom_module_class": {CustomModule: ObservedCustomModule}
}
```