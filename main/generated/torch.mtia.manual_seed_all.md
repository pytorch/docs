# torch.mtia.manual_seed_all

torch.mtia.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/mtia/__init__.py#L478)

Sets the seed for generating random numbers on all MTIA devices.
It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired seed.