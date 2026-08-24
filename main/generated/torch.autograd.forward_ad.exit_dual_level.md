# torch.autograd.forward_ad.exit_dual_level

torch.autograd.forward_ad.exit_dual_level(***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/autograd/forward_ad.py#L47)

Exit a forward grad level.

This function deletes all the gradients associated with this
level. Only deleting the latest entered level is allowed.

This function also updates the current level that is used by default
by the other functions in this API.