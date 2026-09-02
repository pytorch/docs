# torch.cuda.get_rng_state

torch.cuda.get_rng_state(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/random.py#L23)

Return the random number generator state of the specified GPU as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'cuda'` (i.e., `torch.device('cuda')`, the current CUDA device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes CUDA.