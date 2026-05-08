# torch.nn.utils.rnn.pack_sequence

torch.nn.utils.rnn.pack_sequence(*sequences*, *enforce_sorted=True*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/nn/utils/rnn.py#L522)

Packs a list of variable length Tensors.

Consecutive call of the next functions: `pad_sequence`, `pack_padded_sequence`.

`sequences` should be a list of Tensors of size `L x *`, where L is
the length of a sequence and * is any number of trailing dimensions,
including `0`.

For unsorted sequences, use enforce_sorted = False. If `enforce_sorted`
is `True`, the sequences should be sorted in the order of decreasing length.
`enforce_sorted = True` is only necessary for ONNX export.

Example

```
>>> from torch.nn.utils.rnn import pack_sequence
>>> a = torch.tensor([1, 2, 3])
>>> b = torch.tensor([4, 5])
>>> c = torch.tensor([6])
>>> pack_sequence([a, b, c])
PackedSequence(data=tensor([1, 4, 6, 2, 5, 3]), batch_sizes=tensor([3, 2, 1]), sorted_indices=None, unsorted_indices=None)
```

Parameters:

- **sequences** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - A list of sequences of decreasing length.
- **enforce_sorted** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, checks that the input
contains sequences sorted by length in a decreasing order. If
`False`, this condition is not checked. Default: `True`.

Returns:

a [`PackedSequence`](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence) object

Return type:

[*PackedSequence*](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence)