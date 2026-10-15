# torch.mtia.get_rng_state

torch.mtia.get_rng_state(*device='mtia'*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/mtia/__init__.py#L398)

Returns the random number generator state of the specified MTIA device as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'mtia'` (i.e., `torch.device('mtia')`, the current mtia device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes MTIA.