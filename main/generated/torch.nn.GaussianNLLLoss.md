# GaussianNLLLoss

*class*torch.nn.GaussianNLLLoss(***, *full=False*, *eps=1e-06*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/loss.py#L377)

Gaussian negative log likelihood loss.

The targets are treated as samples from Gaussian distributions with
expectations and variances predicted by the neural network. For a
`target` tensor modelled as having Gaussian distribution with a tensor
of expectations `input` and a tensor of positive variances `var` the loss is:

loss=12(log⁡(max(var, eps))+(input−target)2max(var, eps))+const.\text{loss} = \frac{1}{2}\left(\log\left(\text{max}\left(\text{var},
\ \text{eps}\right)\right) + \frac{\left(\text{input} - \text{target}\right)^2}
{\text{max}\left(\text{var}, \ \text{eps}\right)}\right) + \text{const.}

loss=21​(log(max(var, eps))+max(var, eps)(input−target)2​)+const.

where `eps` is used for stability. By default, the constant term of
the loss function is omitted unless `full` is `True`. If `var` is not the same
size as `input` (due to a homoscedastic assumption), it must either have a final dimension
of 1 or have one fewer dimension (with all other sizes being the same) for correct broadcasting.

Parameters:

- **full** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - include the constant term in the loss
calculation. Default: `False`.
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - value used to clamp `var` (see note below), for
stability. Default: 1e-6.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - specifies the reduction to apply to the
output:`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction
will be applied, `'mean'`: the output is the average of all batch
member losses, `'sum'`: the output is the sum of all batch member
losses. Default: `'mean'`.

Shape:

- Input: (N,∗)(N, *)(N,∗) or (∗)(*)(∗) where ∗*∗ means any number of additional
dimensions
- Target: (N,∗)(N, *)(N,∗) or (∗)(*)(∗), same shape as the input, or same shape as the input
but with one dimension equal to 1 (to allow for broadcasting)
- Var: (N,∗)(N, *)(N,∗) or (∗)(*)(∗), same shape as the input, or same shape as the input but
with one dimension equal to 1, or same shape as the input but with one fewer
dimension (to allow for broadcasting), or a scalar value
- Output: scalar if `reduction` is `'mean'` (default) or
`'sum'`. If `reduction` is `'none'`, then (N,∗)(N, *)(N,∗), same
shape as the input

Examples

```
>>> loss = nn.GaussianNLLLoss()
>>> input = torch.randn(5, 2, requires_grad=True)
>>> target = torch.randn(5, 2)
>>> var = torch.ones(5, 2, requires_grad=True) # heteroscedastic
>>> output = loss(input, target, var)
>>> output.backward()
```

```
>>> loss = nn.GaussianNLLLoss()
>>> input = torch.randn(5, 2, requires_grad=True)
>>> target = torch.randn(5, 2)
>>> var = torch.ones(5, 1, requires_grad=True) # homoscedastic
>>> output = loss(input, target, var)
>>> output.backward()
```

Note

The clamping of `var` is ignored with respect to autograd, and so the
gradients are unaffected by it.

Reference:

Nix, D. A. and Weigend, A. S., "Estimating the mean and variance of the
target probability distribution", Proceedings of 1994 IEEE International
Conference on Neural Networks (ICNN'94), Orlando, FL, USA, 1994, pp. 55-60
vol.1, doi: 10.1109/ICNN.1994.374138.

forward(*input*, *target*, *var*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/loss.py#L455)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)