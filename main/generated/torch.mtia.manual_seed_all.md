# torch.mtia.manual_seed_all

torch.mtia.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/mtia/__init__.py#L478)

Sets the seed for generating random numbers on all MTIA devices.
It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.