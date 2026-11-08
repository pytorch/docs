# torch.xpu.seed_all

torch.xpu.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/random.py#L133)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if XPU is not available; in that case, it is silently ignored.