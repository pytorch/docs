# torch.mtia.seed_all

torch.mtia.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/mtia/__init__.py#L512)

Sets the seed for generating random numbers to a random number on all MTIA devices.

It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)