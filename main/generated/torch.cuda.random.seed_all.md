# torch.cuda.random.seed_all

torch.cuda.random.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/random.py#L150)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.