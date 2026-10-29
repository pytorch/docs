# torch.mtia.seed_all

torch.mtia.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/mtia/__init__.py#L512)

Sets the seed for generating random numbers to a random number on all MTIA devices.

It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)