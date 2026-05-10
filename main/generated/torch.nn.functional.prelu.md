# torch.nn.functional.prelu

torch.nn.functional.prelu(*input*, *weight*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/nn/functional.py#L1941)

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