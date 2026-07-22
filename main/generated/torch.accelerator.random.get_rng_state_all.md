# torch.accelerator.random.get_rng_state_all

torch.accelerator.random.get_rng_state_all()[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/accelerator/random.py#L45)

Return a list of torch.Tensor of dtype torch.uint8 representing the RNG states of all devices for
the current [accelerator](../torch.html#accelerators).

Returns:

the RNG states of the default generators for all devices.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[torch.Tensor](../tensors.html#torch.Tensor)]

Warning

This function eagerly initializes the accelerator runtime.