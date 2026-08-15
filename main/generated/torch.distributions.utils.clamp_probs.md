# torch.distributions.utils.clamp_probs

torch.distributions.utils.clamp_probs(*probs*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/distributions/utils.py#L102)

Clamps the probabilities to be in the open interval (0, 1).

The probabilities would be clamped between eps and 1 - eps,
and eps would be the smallest representable positive number for the input data type.

Parameters:

**probs** ([*Tensor*](../tensors.html#torch.Tensor)) - A tensor of probabilities.

Returns:

The clamped probabilities.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Examples

```
>>> probs = torch.tensor([0.0, 0.5, 1.0])
>>> clamp_probs(probs)
tensor([1.1921e-07, 5.0000e-01, 1.0000e+00])
```

```
>>> probs = torch.tensor([0.0, 0.5, 1.0], dtype=torch.float64)
>>> clamp_probs(probs)
tensor([2.2204e-16, 5.0000e-01, 1.0000e+00], dtype=torch.float64)
```