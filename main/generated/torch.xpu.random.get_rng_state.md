# torch.xpu.random.get_rng_state

torch.xpu.random.get_rng_state(*device='xpu'*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/xpu/random.py#L10)

Return the random number generator state of the specified GPU as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'xpu'` (i.e., `torch.device('xpu')`, the current XPU device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes XPU.