# TensorWeakRef

*class*torch.utils.weak.TensorWeakRef(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/utils/weak.py#L349)

Wrapper around a weak ref of a Tensor that handles the _fix_weakref() call required when unwrapping a Tensor weakref.