# torch.xpu.manual_seed_all

torch.xpu.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/xpu/random.py#L97)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired seed.