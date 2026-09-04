# torch.cuda.manual_seed_all

torch.cuda.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/cuda/random.py#L112)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.