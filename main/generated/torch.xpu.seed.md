# torch.xpu.seed

torch.xpu.seed()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/xpu/random.py#L115)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.xpu.seed_all.html#torch.xpu.seed_all).