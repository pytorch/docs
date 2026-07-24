# torch.cuda.random.get_rng_state

torch.cuda.random.get_rng_state(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/random.py#L23)

Return the random number generator state of the specified GPU as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'cuda'` (i.e., `torch.device('cuda')`, the current CUDA device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes CUDA.