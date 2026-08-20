# torch.cuda.seed

torch.cuda.seed()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/random.py#L131)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.cuda.seed_all.html#torch.cuda.seed_all).