# torch.cuda.random.seed

torch.cuda.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/random.py#L131)

Set the seed for generating random numbers to a random number for the current GPU.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Warning

If you are working with a multi-GPU model, this function will only initialize
the seed on one GPU. To initialize all GPUs, use [`seed_all()`](torch.cuda.random.seed_all.html#torch.cuda.random.seed_all).