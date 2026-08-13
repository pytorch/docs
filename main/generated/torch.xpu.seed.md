# torch.xpu.seed

torch.xpu.seed()[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/xpu/random.py#L115)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.xpu.seed_all.html#torch.xpu.seed_all).