# torch.autograd.graph.increment_version

torch.autograd.graph.increment_version(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/autograd/graph.py#L245)

Update autograd metadata tracking whether the given Tensor was modified in place.

This is to enable more accurate error checking within the autograd engine.
It is already done automatically by PyTorch functions and within custom Function
when mark_dirty() is called appropriately so you only need to call this explicitly
if you are doing inplace operation on the Tensor data in a way that Pytorch doesn't
know about. For example a custom kernel that reads the Tensor data_ptr and modifies
the memory inplace based on this pointer. Can accept either a tensor, or a list of tensors.

Note that incrementing the version counter multiple times for a single inplace operation
is not problematic.

Note that if you pass in tensor constructed under torch.inference_mode(),
we will not bump its version counter (because your tensor does not have one).