# torch.cuda.random.manual_seed_all

torch.cuda.random.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/random.py#L112)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.