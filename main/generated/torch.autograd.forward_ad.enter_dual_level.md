# torch.autograd.forward_ad.enter_dual_level

torch.autograd.forward_ad.enter_dual_level()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/autograd/forward_ad.py#L23)

Enter a new forward grad level.

This level can be used to make and unpack dual Tensors to compute
forward gradients.

This function also updates the current level that is used by default
by the other functions in this API.