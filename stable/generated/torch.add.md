# torch.add

torch.add(*input*, *other*, ***, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Adds `other`, scaled by `alpha`, to `input`.

outi=inputi+alpha×otheri\text{{out}}_i = \text{{input}}_i + \text{{alpha}} \times \text{{other}}_i

outi​=inputi​+alpha×otheri​

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer, float, and complex inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - the tensor or number to add to `input`.

Keyword Arguments:

- **alpha** (*Number*) - the multiplier for `other`.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Examples:

```
>>> a = torch.randn(4)
>>> a
tensor([ 0.0202, 1.0985, 1.3506, -0.6056])
>>> torch.add(a, 20)
tensor([ 20.0202, 21.0985, 21.3506, 19.3944])

>>> b = torch.randn(4)
>>> b
tensor([-0.9732, -0.3497, 0.6245, 0.4022])
>>> c = torch.randn(4, 1)
>>> c
tensor([[ 0.3743],
 [-1.7724],
 [-0.5811],
 [-0.8017]])
>>> torch.add(b, c, alpha=10)
tensor([[ 2.7695, 3.3930, 4.3672, 4.1450],
 [-18.6971, -18.0736, -17.0994, -17.3216],
 [ -6.7845, -6.1610, -5.1868, -5.4090],
 [ -8.9902, -8.3667, -7.3925, -7.6147]])
```