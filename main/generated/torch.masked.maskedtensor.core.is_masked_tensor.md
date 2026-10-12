# torch.masked.maskedtensor.core.is_masked_tensor

torch.masked.maskedtensor.core.is_masked_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/44a629b353df33cd84f67a031bba5b6313160a1c/torch/masked/maskedtensor/core.py#L18)

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