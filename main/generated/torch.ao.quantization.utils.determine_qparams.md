# determine_qparams

*class*torch.ao.quantization.utils.determine_qparams(*min_val*, *max_val*, *quant_min*, *quant_max*, *dtype*, *eps*, *has_customized_qrange*, *qscheme=torch.per_tensor_affine*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/ao/quantization/utils.py#L643)

Calculates the quantization parameters, given min and max
value tensors. Works for both per tensor and per channel cases

Parameters:

- **min_val** ([*Tensor*](../tensors.html#torch.Tensor)) - Minimum values per channel
- **max_val** ([*Tensor*](../tensors.html#torch.Tensor)) - Maximum values per channel

Returns:

Scales tensor of shape (#channels,)
zero_points: Zero points tensor of shape (#channels,)

Return type:

scales