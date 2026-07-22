# torch.cuda.random.manual_seed

torch.cuda.random.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/cuda/random.py#L89)

Set the seed for generating random numbers for the current GPU.

It's safe to call this function if CUDA is not available; in that
case, it is silently ignored.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed.

Warning

If you are working with a multi-GPU model, this function is insufficient
to get determinism. To seed all GPUs, use [`manual_seed_all()`](torch.cuda.random.manual_seed_all.html#torch.cuda.random.manual_seed_all).