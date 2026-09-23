# torch.xpu.get_rng_state

torch.xpu.get_rng_state(*device='xpu'*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/xpu/random.py#L10)

Return the random number generator state of the specified GPU as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'xpu'` (i.e., `torch.device('xpu')`, the current XPU device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes XPU.