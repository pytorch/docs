# torch.xpu.manual_seed

torch.xpu.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/xpu/random.py#L75)

Set the seed for generating random numbers for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.

Warning

If you are working with a multi-GPU model, this function is insufficient
to get determinism. To seed all GPUs, use [`manual_seed_all()`](torch.xpu.manual_seed_all.html#torch.xpu.manual_seed_all).