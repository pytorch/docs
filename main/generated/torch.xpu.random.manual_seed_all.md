# torch.xpu.random.manual_seed_all

torch.xpu.random.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/xpu/random.py#L97)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.