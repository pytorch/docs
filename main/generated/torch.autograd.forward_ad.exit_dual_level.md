# torch.autograd.forward_ad.exit_dual_level

torch.autograd.forward_ad.exit_dual_level(***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/autograd/forward_ad.py#L47)

Exit a forward grad level.

This function deletes all the gradients associated with this
level. Only deleting the latest entered level is allowed.

This function also updates the current level that is used by default
by the other functions in this API.