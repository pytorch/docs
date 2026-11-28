# torch.cuda.manual_seed_all

torch.cuda.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/random.py#L112)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired seed.