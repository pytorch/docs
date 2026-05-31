# torch.nn.utils.rnn.pad_sequence

torch.nn.utils.rnn.pad_sequence(*sequences*, *batch_first=False*, *padding_value=0.0*, *padding_side='right'*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/nn/utils/rnn.py#L405)

Pad a list of variable length Tensors with `padding_value`.

`pad_sequence` stacks a list of Tensors along a new dimension, and pads them
to equal length. `sequences` can be list of sequences with size `L x *`,
where L is length of the sequence and `*` is any number of dimensions
(including `0`). If `batch_first` is `False`, the output is of size
`T x B x *`, and `B x T x *` otherwise, where `B` is the batch size
(the number of elements in `sequences`), `T` is the length of the longest
sequence.

Example

```
>>> from torch.nn.utils.rnn import pad_sequence
>>> a = torch.ones(25, 300)
>>> b = torch.ones(22, 300)
>>> c = torch.ones(15, 300)
>>> pad_sequence([a, b, c]).size()
torch.Size([25, 3, 300])
```

Note

This function returns a Tensor of size `T x B x *` or `B x T x *`
where T is the length of the longest sequence. This function assumes
trailing dimensions and type of all the Tensors in sequences are same.

Parameters:

- **sequences** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - list of variable length sequences.
- **batch_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, the output will be in `B x T x *`
format, `T x B x *` otherwise.
- **padding_value** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - value for padded elements. Default: `0`.
- **padding_side** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - the side to pad the sequences on.
Default: `'right'`.

Returns:

Tensor of size `T x B x *` if `batch_first` is `False`.
Tensor of size `B x T x *` otherwise

Return type:

[*Tensor*](../tensors.html#torch.Tensor)