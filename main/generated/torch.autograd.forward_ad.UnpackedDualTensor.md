# UnpackedDualTensor

*class*torch.autograd.forward_ad.UnpackedDualTensor(*primal*, *tangent*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/autograd/forward_ad.py#L141)

Namedtuple returned by [`unpack_dual()`](torch.autograd.forward_ad.unpack_dual.html#torch.autograd.forward_ad.unpack_dual) containing the primal and tangent components of the dual tensor.

See [`unpack_dual()`](torch.autograd.forward_ad.unpack_dual.html#torch.autograd.forward_ad.unpack_dual) for more details.

count(*value*, */*)

Return number of occurrences of value.

index(*value*, *start=0*, *stop=9223372036854775807*, */*)

Return first index of value.

Raises ValueError if the value is not present.

primal*: [Tensor](../tensors.html#torch.Tensor)*

Alias for field number 0

tangent*: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

Alias for field number 1