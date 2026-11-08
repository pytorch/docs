# TensorWeakRef

*class*torch.utils.weak.TensorWeakRef(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/utils/weak.py#L349)

Wrapper around a weak ref of a Tensor that handles the _fix_weakref() call required when unwrapping a Tensor weakref.