# torch.cuda.random.seed

torch.cuda.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/random.py#L131)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.cuda.random.seed_all.html#torch.cuda.random.seed_all).