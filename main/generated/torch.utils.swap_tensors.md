# torch.utils.swap_tensors

torch.utils.swap_tensors(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/utils/__init__.py#L47)

This function swaps the content of the two Tensor objects.
At a high level, this will make t1 have the content of t2 while preserving
its identity.

This will not work if t1 and t2 have different slots.