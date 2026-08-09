# torch.mtia.seed

torch.mtia.seed()[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/mtia/__init__.py#L495)

Sets the seed for generating random numbers to a random number for the current MTIA device.
It's safe to call this function if MTIA is not available; in that case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.mtia.seed_all.html#torch.mtia.seed_all).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)