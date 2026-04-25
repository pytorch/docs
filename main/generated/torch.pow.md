# torch.pow

torch.pow(*input*, *exponent*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Takes the power of each element in `input` with `exponent` and
returns a tensor with the result.

`exponent` can be either a single `float` number or a Tensor
with the same number of elements as `input`.

When `exponent` is a scalar value, the operation applied is:

outi=xiexponent\text{out}_i = x_i ^ \text{exponent}

outi​=xiexponent​

When `exponent` is a tensor, the operation applied is:

outi=xiexponenti\text{out}_i = x_i ^ {\text{exponent}_i}

outi​=xiexponenti​​

When `exponent` is a tensor, the shapes of `input`
and `exponent` must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **exponent** ([*float*](https://docs.python.org/3/library/functions.html#float)*or**tensor*) - the exponent value

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([ 0.4331, 1.2475, 0.6834, -0.2791])
>>> torch.pow(a, 2)
tensor([ 0.1875, 1.5561, 0.4670, 0.0779])
>>> exp = torch.arange(1., 5.)

>>> a = torch.arange(1., 5.)
>>> a
tensor([ 1., 2., 3., 4.])
>>> exp
tensor([ 1., 2., 3., 4.])
>>> torch.pow(a, exp)
tensor([ 1., 4., 27., 256.])
```

torch.pow(*self*, *exponent*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

`self` is a scalar `float` value, and `exponent` is a tensor.
The returned tensor `out` is of the same shape as `exponent`

The operation applied is:

outi=selfexponenti\text{out}_i = \text{self} ^ {\text{exponent}_i}

outi​=selfexponenti​
Parameters:

- **self** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the scalar base value for the power operation
- **exponent** ([*Tensor*](../tensors.html#torch.Tensor)) - the exponent tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> exp = torch.arange(1., 5.)
>>> base = 2
>>> torch.pow(base, exp)
tensor([ 2., 4., 8., 16.])
```