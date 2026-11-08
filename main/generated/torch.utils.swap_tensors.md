# torch.utils.swap_tensors

torch.utils.swap_tensors(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/utils/__init__.py#L47)

This function swaps the content of the two Tensor objects.
At a high level, this will make t1 have the content of t2 while preserving
its identity.

This will not work if t1 and t2 have different slots.