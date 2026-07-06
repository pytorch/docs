# torch.autograd.forward_ad.exit_dual_level

torch.autograd.forward_ad.exit_dual_level(***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/autograd/forward_ad.py#L47)

Exit a forward grad level.

This function deletes all the gradients associated with this
level. Only deleting the latest entered level is allowed.

This function also updates the current level that is used by default
by the other functions in this API.