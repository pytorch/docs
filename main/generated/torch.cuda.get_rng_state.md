# torch.cuda.get_rng_state

torch.cuda.get_rng_state(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/random.py#L23)

Return the random number generator state of the specified GPU as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'cuda'` (i.e., `torch.device('cuda')`, the current CUDA device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes CUDA.