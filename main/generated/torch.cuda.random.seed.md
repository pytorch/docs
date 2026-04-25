# torch.cuda.random.seed

torch.cuda.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/cuda/random.py#L131)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.cuda.random.seed_all.html#torch.cuda.random.seed_all).