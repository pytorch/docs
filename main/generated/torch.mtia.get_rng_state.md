# torch.mtia.get_rng_state

torch.mtia.get_rng_state(*device='mtia'*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/mtia/__init__.py#L398)

Returns the random number generator state of the specified MTIA device as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'mtia'` (i.e., `torch.device('mtia')`, the current mtia device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes MTIA.