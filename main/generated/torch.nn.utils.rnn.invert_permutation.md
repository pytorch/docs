# torch.nn.utils.rnn.invert_permutation

torch.nn.utils.rnn.invert_permutation(*permutation*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/utils/rnn.py#L240)

Returns the inverse of `permutation`.

This is useful for converting between sorted and unsorted indices in
a `PackedSequence`.

Parameters:

**permutation** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a 1-D tensor of indices to invert

Return type:

[*Tensor*](../tensors.html#torch.Tensor) | None