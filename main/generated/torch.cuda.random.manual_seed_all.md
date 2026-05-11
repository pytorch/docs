# torch.cuda.random.manual_seed_all

torch.cuda.random.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/cuda/random.py#L112)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.