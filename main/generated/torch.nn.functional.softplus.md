# torch.nn.functional.softplus

torch.nn.functional.softplus(*input*, *beta=1*, *threshold=20*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/functional.py#L2115)

Applies element-wise, the function Softplus(x)=1β∗log⁡(1+exp⁡(β∗x))\text{Softplus}(x) = \frac{1}{\beta} * \log(1 + \exp(\beta * x))Softplus(x)=β1​∗log(1+exp(β∗x)).

For numerical stability the implementation reverts to the linear function
when input×β>thresholdinput \times \beta > thresholdinput×β>threshold.

See [`Softplus`](torch.nn.Softplus.html#torch.nn.Softplus) for more details.