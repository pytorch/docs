# torch.mtia.seed_all

torch.mtia.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/mtia/__init__.py#L512)

Sets the seed for generating random numbers to a random number on all MTIA devices.

It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)