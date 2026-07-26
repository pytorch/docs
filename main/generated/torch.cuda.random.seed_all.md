# torch.cuda.random.seed_all

torch.cuda.random.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cuda/random.py#L150)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.