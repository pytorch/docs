# torch.nn.utils.rnn.invert_permutation

torch.nn.utils.rnn.invert_permutation(*permutation*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/utils/rnn.py#L240)

Returns the inverse of `permutation`.

This is useful for converting between sorted and unsorted indices in
a `PackedSequence`.

Parameters:

**permutation** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a 1-D tensor of indices to invert

Return type:

[*Tensor*](../tensors.html#torch.Tensor) | None