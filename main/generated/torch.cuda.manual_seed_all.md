# torch.cuda.manual_seed_all

torch.cuda.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/cuda/random.py#L112)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired seed.