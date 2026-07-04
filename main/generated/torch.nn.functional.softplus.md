# torch.nn.functional.softplus

torch.nn.functional.softplus(*input*, *beta=1*, *threshold=20*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/nn/functional.py#L2115)

Applies element-wise, the function Softplus(x)=1β∗log⁡(1+exp⁡(β∗x))\text{Softplus}(x) = \frac{1}{\beta} * \log(1 + \exp(\beta * x))Softplus(x)=β1​∗log(1+exp(β∗x)).

For numerical stability the implementation reverts to the linear function
when input×β>thresholdinput \times \beta > thresholdinput×β>threshold.

See [`Softplus`](torch.nn.Softplus.html#torch.nn.Softplus) for more details.