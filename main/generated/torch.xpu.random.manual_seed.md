# torch.xpu.random.manual_seed

torch.xpu.random.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/xpu/random.py#L75)

Set the seed for generating random numbers for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.

Warning

If you are working with a multi-GPU model, this function is insufficient
to get determinism. To seed all GPUs, use [`manual_seed_all()`](torch.xpu.random.manual_seed_all.html#torch.xpu.random.manual_seed_all).