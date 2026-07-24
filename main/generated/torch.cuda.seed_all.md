# torch.cuda.seed_all

torch.cuda.seed_all()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/random.py#L150)

Set the seed for generating random numbers to a random number on all GPUs.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.