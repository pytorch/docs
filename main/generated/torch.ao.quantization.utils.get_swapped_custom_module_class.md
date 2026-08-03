# get_swapped_custom_module_class

*class*torch.ao.quantization.utils.get_swapped_custom_module_class(*custom_module*, *custom_module_class_mapping*, *qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/ao/quantization/utils.py#L240)

Get the observed/quantized custom module class that we need
to swap `custom_module` to.

Input:

- custom_module: input, can be an instance of either a float or observed custom module
- custom_module_class_mapping: the float to observed or observed to quantized custom module class mapping
- qconfig: qconfig configured for the custom module

Output:

Corresponding observed/quantized custom module class for input custom module instance.