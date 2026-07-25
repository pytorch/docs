# torch.autograd.forward_ad.exit_dual_level

torch.autograd.forward_ad.exit_dual_level(***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/autograd/forward_ad.py#L47)

Exit a forward grad level.

This function deletes all the gradients associated with this
level. Only deleting the latest entered level is allowed.

This function also updates the current level that is used by default
by the other functions in this API.