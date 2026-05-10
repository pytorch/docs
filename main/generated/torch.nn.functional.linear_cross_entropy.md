# torch.nn.functional.linear_cross_entropy

torch.nn.functional.linear_cross_entropy(*input*, *linear_weight*, *target*, ***, *weight=None*, *reduction='mean'*, *ignore_index=None*, *label_smoothing=0.0*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/nn/functional.py#L3656)

Compute the cross entropy loss between inputs, transformed linearly, and target.

The statement:

```
loss = linear_cross_entropy(input, linear_weight, target, **kwargs)
```

is equivalent to the following reference implementation of linear_cross_entropy:

```
logits = linear(input, linear_weight)
loss = cross_entropy(logits, target, **kwargs)
```

provided that `ignore_index` is not explicitly set to None
in kwargs (since [`cross_entropy()`](torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy) does not accept None
for `ignore_index`).

See [`Linear`](torch.nn.Linear.html#torch.nn.Linear) and [`CrossEntropyLoss`](torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input samples.
- **linear_weight** ([*Tensor*](../tensors.html#torch.Tensor)) - linear weight.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth class indices or class probabilities;
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight given to each class.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to
the output: `'none'` | `'mean'` |
`'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the
number of elements in the output, `'sum'`: the output
will be summed.
Default: `'mean'`.
- **ignore_index** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Specifies a target value that is
ignored and does not contribute to the input
gradient. Note that `ignore_index` is only
applicable when the target contains class indices.
Default: None. When target contains class indices, the
default value is mapped to -100. Note: the default
`ignore_index` in
[`cross_entropy`](torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy) is -100 for both
target types.
- **label_smoothing** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - A float in [0.0, 1.0].
Specifies the amount of smoothing when computing the
loss, where 0.0 means no smoothing. The targets become a
mixture of the original ground truth and a uniform
distribution as described in [Rethinking the Inception
Architecture for Computer Vision](https://arxiv.org/abs/1512.00567).
Default: 0.00.00.0.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Shape:

- Input: (infeatures)(in_features)(inf​eatures) or (N,in_features)(N, in\_features)(N,in_features).
- Linear weight: (C,in_features)(C, in\_features)(C,in_features) or (C,d1,...,dK,in_features)(C, d_1,
..., d_K, in\_features)(C,d1​,...,dK​,in_features) with K≥1K \geq 1K≥1 in the case of
K-dimensional loss. Note: multi-dimensional weights (K > 0)
require batched input (N,in_features)(N, in\_features)(N,in_features).
- Target: If containing class indices, ()()(),
(N)(N)(N), or (N,d1,d2,...,dK)(N, d_1, d_2, ..., d_K)(N,d1​,d2​,...,dK​) when
K≥1K\geq 1K≥1, where each value should be between
[0,C)[0, C)[0,C). The target data type is required to be long
when using class indices.
If containing class probabilities, the target must have
shape (C)(C)(C), (N,C)(N, C)(N,C), or (N,C,d1,d2,...,dK)(N, C, d_1,
d_2, ..., d_K)(N,C,d1​,d2​,...,dK​) when K≥1K\geq 1K≥1, and each value should
be between [0,1][0, 1][0,1]. This means the target data type
is required to be float when using class probabilities. Note
that PyTorch does not strictly enforce probability
constraints on the class probabilities and that it is the
user's responsibility to ensure `target` contains valid
probability distributions.
- Weight: (C)(C)(C).
- Output: If reduction is 'none', shape ()()(),
(N)(N)(N) or (N,d1,d2,...,dK)(N, d_1, d_2, ..., d_K)(N,d1​,d2​,...,dK​) with K≥1K\geq 1K≥1
in the case of K-dimensional loss, depending on the
shape of the input. Otherwise, scalar.

where NNN is batch size and CCC is number of classes.