# torch.mtia.get_rng_state

torch.mtia.get_rng_state(*device='mtia'*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/mtia/__init__.py#L398)

Returns the random number generator state of the specified MTIA device as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'mtia'` (i.e., `torch.device('mtia')`, the current mtia device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes MTIA.