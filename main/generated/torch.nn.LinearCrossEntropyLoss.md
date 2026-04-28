# LinearCrossEntropyLoss

*class*torch.nn.LinearCrossEntropyLoss(*in_features*, *num_classes*, ***, *out_features=()*, *device=None*, *dtype=None*, *reduction='mean'*, *weight=None*, *ignore_index=None*, *label_smoothing=0.0*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/nn/modules/loss.py#L1407)

This criterion computes the cross entropy loss between input,
linearly transformed to logits, and target.

See [`CrossEntropyLoss`](torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) for the definition of cross entropy loss.

Parameters:

- **in_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Size of each input sample.
- **num_classes** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of classes, CCC.
- **out_features** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - specifies dimensions
(d1,d2,...,dK)(d_1, d_2, ..., d_K)(d1​,d2​,...,dK​) for K-dimensional loss.
Default: `()`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device
of linear weight. Default: `None`.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired dtype of
linear weight. Default: `None`.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight given to
each class. If given, has to be a Tensor of size C.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to
the output: `'none'` | `'mean'` | `'sum'`.
`'none'`: no reduction will be applied,
`'mean'`: the weighted mean of the output is taken,
`'sum'`: the output will be summed.
Default: `'mean'`.
- **ignore_index** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Specifies a target value that is
ignored and does not contribute to the input
gradient. Note that `ignore_index` is only
applicable when the target contains class indices.
Default: None. When target contains class indices, the
default value is mapped to -100. Note: the default
`ignore_index` in
[`CrossEntropyLoss`](torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) is -100 for both
target types.
- **label_smoothing** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - A float in [0.0, 1.0].
Specifies the amount of smoothing when computing the loss,
where 0.0 means no smoothing. The targets become a mixture
of the original ground truth and a uniform distribution as
described in [Rethinking the Inception Architecture for
Computer Vision](https://arxiv.org/abs/1512.00567).
Default: 0.00.00.0.

Shape:

- Input: Shape (infeatures)(in_features)(inf​eatures), (N,infeatures)(N, in_features)(N,inf​eatures).
- Target: If containing class indices, shape ()()(),
(N)(N)(N) or (N,∗outfeatures)(N, *out_features)(N,∗outf​eatures) where each value
should be between [0,C)[0, C)[0,C). The target data type is
required to be long when using class indices.
If containing class probabilities, the target must have
shape (C)(C)(C) or (N,C,∗outfeatures)(N, C, *out_features)(N,C,∗outf​eatures), and
each value should be between [0,1][0, 1][0,1]. This means the
target data type is required to be float when using class
probabilities. Note that PyTorch does not strictly enforce
probability constraints on the class probabilities and that
it is the user's responsibility to ensure `target`
contains valid probability distributions (see below examples
section for more details).
- Output: If reduction is 'none', shape ()()(),
(N)(N)(N) or (N,∗outfeatures)(N, *out_features)(N,∗outf​eatures) depending on the
shape of the input. Otherwise, scalar.

where NNN is batch size.

Examples

```
>>> torch.manual_seed(283)
>>> # Example of target with class indices
>>> loss = nn.LinearCrossEntropyLoss(5, 10, out_features=(4, 3))
>>> input = torch.randn(2, 5, requires_grad=True)
>>> target = torch.randint(0, 10, (2, 4, 3))
>>> output = loss(input, target)
>>> output.backward()
>>>
>>> # Example of target with class probabilities
>>> input = torch.randn(2, 5, requires_grad=True)
>>> target = torch.randn(2, 10, 4, 3).softmax(dim=1)
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/nn/modules/loss.py#L1540)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)