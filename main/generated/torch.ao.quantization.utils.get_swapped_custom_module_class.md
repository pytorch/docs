# get_swapped_custom_module_class

*class*torch.ao.quantization.utils.get_swapped_custom_module_class(*custom_module*, *custom_module_class_mapping*, *qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/ao/quantization/utils.py#L240)

Get the observed/quantized custom module class that we need
to swap `custom_module` to.

Input:

- custom_module: input, can be an instance of either a float or observed custom module
- custom_module_class_mapping: the float to observed or observed to quantized custom module class mapping
- qconfig: qconfig configured for the custom module

Output:

Corresponding observed/quantized custom module class for input custom module instance.