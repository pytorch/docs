# torch.nn.functional.prelu

torch.nn.functional.prelu(*input*, *weight*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/functional.py#L1989)

Applies element-wise the function
PReLU(x)=max⁡(0,x)+weight∗min⁡(0,x)\text{PReLU}(x) = \max(0,x) + \text{weight} * \min(0,x)PReLU(x)=max(0,x)+weight∗min(0,x) where weight is a
learnable parameter.

Note

weight is expected to be a scalar or 1-D tensor. If weight is 1-D,
its size must match the number of input channels, determined by
input.size(1) when input.dim() >= 2, otherwise 1.
In the 1-D case, note that when input has dim > 2, weight can be expanded
to the shape of input in a way that is not possible using normal
[broadcasting semantics](../notes/broadcasting.html#broadcasting-semantics).

See [`PReLU`](torch.nn.PReLU.html#torch.nn.PReLU) for more details.