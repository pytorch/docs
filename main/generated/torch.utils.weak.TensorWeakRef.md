# TensorWeakRef

*class*torch.utils.weak.TensorWeakRef(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/utils/weak.py#L349)

Wrapper around a weak ref of a Tensor that handles the _fix_weakref() call required when unwrapping a Tensor weakref.