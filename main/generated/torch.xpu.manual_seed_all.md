# torch.xpu.manual_seed_all

torch.xpu.manual_seed_all(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/xpu/random.py#L97)

Set the seed for generating random numbers on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.