# torch.bitwise_right_shift

torch.bitwise_right_shift(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the right arithmetic shift of `input` by `other` bits.
The input tensor must be of integral type. This operator supports
[broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics) and
[type promotion](../tensor_attributes.html#type-promotion-doc).
In any case, if the value of the right operand is negative or is greater
or equal to the number of bits in the promoted left operand, the behavior is undefined.

The operation applied is:

outi=inputi>>otheri\text{out}_i = \text{input}_i >> \text{other}_i

outi​=inputi​>>otheri​
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - the first input tensor
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.bitwise_right_shift(torch.tensor([-2, -7, 31], dtype=torch.int8), torch.tensor([1, 0, 3], dtype=torch.int8))
tensor([-1, -7, 3], dtype=torch.int8)
```