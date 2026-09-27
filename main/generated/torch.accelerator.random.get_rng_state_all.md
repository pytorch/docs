# torch.accelerator.random.get_rng_state_all

torch.accelerator.random.get_rng_state_all()[[source]](https://github.com/pytorch/pytorch/blob/8bea8e2d91031a1dee02417397d5a065e31c43c8/torch/accelerator/random.py#L46)

Return a list of torch.Tensor of dtype torch.uint8 representing the RNG states of all devices for
the current [accelerator](../torch.html#accelerators).

Returns:

the RNG states of the default generators for all devices.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[torch.Tensor](../tensors.html#torch.Tensor)]

Warning

This function eagerly initializes the accelerator runtime.