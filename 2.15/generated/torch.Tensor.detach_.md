# torch.Tensor.detach_

Tensor.detach_()

Detaches the Tensor from the graph that created it, making it a leaf.
Views cannot be detached in-place.

This method also affects forward mode AD gradients and the result will never
have forward mode AD gradients.