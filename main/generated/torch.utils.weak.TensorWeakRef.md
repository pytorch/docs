# TensorWeakRef

*class*torch.utils.weak.TensorWeakRef(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/utils/weak.py#L349)

Wrapper around a weak ref of a Tensor that handles the _fix_weakref() call required when unwrapping a Tensor weakref.