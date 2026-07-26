# torch.xpu.seed_all

torch.xpu.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/xpu/random.py#L133)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.