# torch.autograd.forward_ad.enter_dual_level

torch.autograd.forward_ad.enter_dual_level()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/autograd/forward_ad.py#L23)

Enter a new forward grad level.

This level can be used to make and unpack dual Tensors to compute
forward gradients.

This function also updates the current level that is used by default
by the other functions in this API.