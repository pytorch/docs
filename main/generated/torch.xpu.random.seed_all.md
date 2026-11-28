# torch.xpu.random.seed_all

torch.xpu.random.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/xpu/random.py#L133)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.