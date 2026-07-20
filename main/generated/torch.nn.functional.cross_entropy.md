# torch.nn.functional.cross_entropy

torch.nn.functional.cross_entropy(*input*, *target*, *weight=None*, *size_average=None*, *ignore_index=-100*, *reduce=None*, *reduction='mean'*, *label_smoothing=0.0*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/nn/functional.py#L3478)

Compute the cross entropy loss between input logits and target.

See [`CrossEntropyLoss`](torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted unnormalized logits;
see Shape section below for supported shapes.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth class indices or class probabilities;
see Shape section below for supported shapes.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight given to each
class. If given, has to be a Tensor of size C
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **ignore_index** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Specifies a target value that is ignored
and does not contribute to the input gradient. When `size_average` is
`True`, the loss is averaged over non-ignored targets. Note that
`ignore_index` is only applicable when the target contains class indices.
Default: -100
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`
- **label_smoothing** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - A float in [0.0, 1.0]. Specifies the amount
of smoothing when computing the loss, where 0.0 means no smoothing. The targets
become a mixture of the original ground truth and a uniform distribution as described in
[Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567). Default: 0.00.00.0.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Shape:

- Input: Shape (C)(C)(C), (N,C)(N, C)(N,C) or (N,C,d1,d2,...,dK)(N, C, d_1, d_2, ..., d_K)(N,C,d1​,d2​,...,dK​) with K≥1K \geq 1K≥1
in the case of K-dimensional loss.
- Target: If containing class indices, shape ()()(), (N)(N)(N) or (N,d1,d2,...,dK)(N, d_1, d_2, ..., d_K)(N,d1​,d2​,...,dK​) with
K≥1K \geq 1K≥1 in the case of K-dimensional loss where each value should be between [0,C)[0, C)[0,C).
If containing class probabilities, same shape as the input and each value should be between [0,1][0, 1][0,1].

where:

C=number of classesN=batch size\begin{aligned}
 C ={} & \text{number of classes} \\
 N ={} & \text{batch size} \\
\end{aligned}

C=N=​number of classesbatch size​

Examples:

```
>>> # Example of target with class indices
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randint(5, (3,), dtype=torch.int64)
>>> loss = F.cross_entropy(input, target)
>>> loss.backward()
>>>
>>> # Example of target with class probabilities
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5).softmax(dim=1)
>>> loss = F.cross_entropy(input, target)
>>> loss.backward()
```