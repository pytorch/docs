# torch.where

torch.where(*condition*, *input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Return a tensor of elements selected from either `input` or `other`, depending on `condition`.

The operation is defined as:

outi={inputiif conditioniotheriotherwise\text{out}_i = \begin{cases}
 \text{input}_i & \text{if } \text{condition}_i \\
 \text{other}_i & \text{otherwise} \\
\end{cases}

outi​={inputi​otheri​​if conditioni​otherwise​

Note

The tensors `condition`, `input`, `other` must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **condition** (*BoolTensor*) - When True (nonzero), yield input, otherwise yield other
- **input** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - value (if `input` is a scalar) or values selected at indices
where `condition` is `True`
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - value (if `other` is a scalar) or values selected at indices
where `condition` is `False`

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Returns:

A tensor of shape equal to the broadcasted shape of `condition`, `input`, `other`

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> x = torch.randn(3, 2)
>>> y = torch.ones(3, 2)
>>> x
tensor([[-0.4620, 0.3139],
 [ 0.3898, -0.7197],
 [ 0.0478, -0.1657]])
>>> torch.where(x > 0, 1.0, 0.0)
tensor([[0., 1.],
 [1., 0.],
 [1., 0.]])
>>> torch.where(x > 0, x, y)
tensor([[ 1.0000, 0.3139],
 [ 0.3898, 1.0000],
 [ 0.0478, 1.0000]])
>>> x = torch.randn(2, 2, dtype=torch.double)
>>> x
tensor([[ 1.0779, 0.0383],
 [-0.8785, -1.1089]], dtype=torch.float64)
>>> torch.where(x > 0, x, 0.)
tensor([[1.0779, 0.0383],
 [0.0000, 0.0000]], dtype=torch.float64)
```

torch.where(*condition*) → tuple of LongTensor

`torch.where(condition)` is identical to
`torch.nonzero(condition, as_tuple=True)`.

Note

See also [`torch.nonzero()`](torch.nonzero.html#torch.nonzero).