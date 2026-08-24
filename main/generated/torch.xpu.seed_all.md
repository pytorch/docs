# torch.xpu.seed_all

torch.xpu.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/xpu/random.py#L133)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.