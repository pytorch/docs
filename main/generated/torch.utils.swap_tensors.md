# torch.utils.swap_tensors

torch.utils.swap_tensors(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/utils/__init__.py#L35)

This function swaps the content of the two Tensor objects.
At a high level, this will make t1 have the content of t2 while preserving
its identity.

This will not work if t1 and t2 have different slots.