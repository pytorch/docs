# torch.masked.maskedtensor.core.is_masked_tensor

torch.masked.maskedtensor.core.is_masked_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/masked/maskedtensor/core.py#L18)

Returns True if the input is a MaskedTensor, else False

Parameters:

**a** - any input

Return type:

*TypeIs*[*MaskedTensor*]

Examples

```
>>> from torch.masked import MaskedTensor
>>> data = torch.arange(6).reshape(2, 3)
>>> mask = torch.tensor([[True, False, False], [True, True, False]])
>>> mt = MaskedTensor(data, mask)
>>> is_masked_tensor(mt)
True
```