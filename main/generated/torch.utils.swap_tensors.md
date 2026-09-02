# torch.utils.swap_tensors

torch.utils.swap_tensors(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/utils/__init__.py#L35)

This function swaps the content of the two Tensor objects.
At a high level, this will make t1 have the content of t2 while preserving
its identity.

This will not work if t1 and t2 have different slots.