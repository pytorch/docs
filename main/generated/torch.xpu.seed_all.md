# torch.xpu.seed_all

torch.xpu.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/xpu/random.py#L133)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.