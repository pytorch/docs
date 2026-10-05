# torch.sub

torch.sub(*input*, *other*, ***, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Subtracts `other`, scaled by `alpha`, from `input`.

outi=inputi−alpha×otheri\text{{out}}_i = \text{{input}}_i - \text{{alpha}} \times \text{{other}}_i

outi​=inputi​−alpha×otheri​

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer, float, and complex inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - the tensor or number to subtract from `input`.

Keyword Arguments:

- **alpha** (*Number*) - the multiplier for `other`.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor((1, 2))
>>> b = torch.tensor((0, 1))
>>> torch.sub(a, b, alpha=2)
tensor([1, 0])
```