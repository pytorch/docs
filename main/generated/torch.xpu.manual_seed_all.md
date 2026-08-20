# torch.xpu.manual_seed_all

torch.xpu.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/xpu/random.py#L97)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.