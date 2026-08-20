# TensorWeakRef

*class*torch.utils.weak.TensorWeakRef(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/utils/weak.py#L349)

Wrapper around a weak ref of a Tensor that handles the _fix_weakref() call required when unwrapping a Tensor weakref.