# torch.nn.functional.softplus

torch.nn.functional.softplus(*input*, *beta=1*, *threshold=20*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/nn/functional.py#L2067)

Applies element-wise, the function Softplus(x)=1β∗log⁡(1+exp⁡(β∗x))\text{Softplus}(x) = \frac{1}{\beta} * \log(1 + \exp(\beta * x))Softplus(x)=β1​∗log(1+exp(β∗x)).

For numerical stability the implementation reverts to the linear function
when input×β>thresholdinput \times \beta > thresholdinput×β>threshold.

See [`Softplus`](torch.nn.Softplus.html#torch.nn.Softplus) for more details.