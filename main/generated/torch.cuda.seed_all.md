# torch.cuda.seed_all

torch.cuda.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/random.py#L150)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.