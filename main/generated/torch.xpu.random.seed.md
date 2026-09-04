# torch.xpu.random.seed

torch.xpu.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/xpu/random.py#L115)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.xpu.random.seed_all.html#torch.xpu.random.seed_all).