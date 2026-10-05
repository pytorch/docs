# torch.Tensor.bernoulli_

Tensor.bernoulli_(*p=0.5*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills each location of `self` with an independent sample from
Bernoulli(p)\text{Bernoulli}(\texttt{p})Bernoulli(p). `self` can have integral
`dtype`.

`p` should either be a scalar or tensor containing probabilities to be
used for drawing the binary random number.

If it is a tensor, the ith\text{i}^{th}ith element of `self` tensor
will be set to a value sampled from
Bernoulli(p_tensor[i])\text{Bernoulli}(\texttt{p\_tensor[i]})Bernoulli(p_tensor[i]). In this case p must have
floating point `dtype`.

See also [`bernoulli()`](torch.Tensor.bernoulli.html#torch.Tensor.bernoulli) and [`torch.bernoulli()`](torch.bernoulli.html#torch.bernoulli)