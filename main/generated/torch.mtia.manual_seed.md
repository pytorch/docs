# torch.mtia.manual_seed

torch.mtia.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/mtia/__init__.py#L457)

Sets the seed for generating random numbers for the current MTIA device.
It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.

Warning

If you are working with a multi-GPU model, this function is insufficient
to get determinism. To seed all GPUs, use [`manual_seed_all()`](torch.mtia.manual_seed_all.html#torch.mtia.manual_seed_all).