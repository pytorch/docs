# torch.Tensor.permute

Tensor.permute(**dims*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of the tensor with its dimensions permuted.

Parameters:

**dims** ([*torch.Size*](../size.html#torch.Size)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*...**,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the desired ordering of dimensions.

Example

```
>>> x = torch.randn(2, 3, 5)
>>> x.size()
torch.Size([2, 3, 5])
>>> x.permute(2, 0, 1).size()
torch.Size([5, 2, 3])
```