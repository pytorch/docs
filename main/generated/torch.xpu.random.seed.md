# torch.xpu.random.seed

torch.xpu.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/xpu/random.py#L115)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.xpu.random.seed_all.html#torch.xpu.random.seed_all).