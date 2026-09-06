# CosineEmbeddingLoss

*class*torch.nn.modules.loss.CosineEmbeddingLoss(*margin=0.0*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/loss.py#L1671)

Creates a criterion that measures the loss given input tensors
x1x_1x1​, x2x_2x2​ and a Tensor label yyy with values 1 or -1.
Use (y=1y=1y=1) to maximize the cosine similarity of two inputs, and (y=−1y=-1y=−1) otherwise.
This is typically used for learning nonlinear
embeddings or semi-supervised learning.

The loss function for each sample is:

loss(x,y)={1−cos⁡(x1,x2),if y=1max⁡(0,cos⁡(x1,x2)−margin),if y=−1\text{loss}(x, y) =
\begin{cases}
1 - \cos(x_1, x_2), & \text{if } y = 1 \\
\max(0, \cos(x_1, x_2) - \text{margin}), & \text{if } y = -1
\end{cases}

loss(x,y)={1−cos(x1​,x2​),max(0,cos(x1​,x2​)−margin),​if y=1if y=−1​
Parameters:

- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Should be a number from −1-1−1 to 111,
000 to 0.50.50.5 is suggested. If `margin` is missing, the
default value is 000.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`). By default,
the losses are averaged over each loss element in the batch. Note that for
some losses, there are multiple elements per sample. If the field `size_average`
is set to `False`, the losses are instead summed for each minibatch. Ignored
when `reduce` is `False`. Default: `True`
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`). By default, the
losses are averaged or summed over observations for each minibatch depending
on `size_average`. When `reduce` is `False`, returns a loss per
batch element instead and ignores `size_average`. Default: `True`
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`

Shape:

- Input1: (N,D)(N, D)(N,D) or (D)(D)(D), where N is the batch size and D is the embedding dimension.
- Input2: (N,D)(N, D)(N,D) or (D)(D)(D), same shape as Input1.
- Target: (N)(N)(N) or ()()().
- Output: If `reduction` is `'none'`, then (N)(N)(N), otherwise scalar.

Examples

```
>>> loss = nn.CosineEmbeddingLoss()
>>> input1 = torch.randn(3, 5, requires_grad=True)
>>> input2 = torch.randn(3, 5, requires_grad=True)
>>> target = torch.ones(3)
>>> output = loss(input1, input2, target)
>>> output.backward()
```

forward(*input1*, *input2*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/loss.py#L1736)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)