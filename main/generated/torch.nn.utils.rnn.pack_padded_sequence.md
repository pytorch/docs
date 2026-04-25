# torch.nn.utils.rnn.pack_padded_sequence

torch.nn.utils.rnn.pack_padded_sequence(*input*, *lengths*, *batch_first=False*, *enforce_sorted=True*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/nn/utils/rnn.py#L258)

Packs a Tensor containing padded sequences of variable length.

`input` can be of size `T x B x *` (if `batch_first` is `False`)
or `B x T x *` (if `batch_first` is `True`) where `T` is the length
of the longest sequence, `B` is the batch size, and `*` is any number of dimensions
(including 0).

For unsorted sequences, use enforce_sorted = False. If `enforce_sorted` is
`True`, the sequences should be sorted by length in a decreasing order, i.e.
`input[:,0]` should be the longest sequence, and `input[:,B-1]` the shortest
one. enforce_sorted = True is only necessary for ONNX export.

It is an inverse operation to [`pad_packed_sequence()`](torch.nn.utils.rnn.pad_packed_sequence.html#torch.nn.utils.rnn.pad_packed_sequence), and hence [`pad_packed_sequence()`](torch.nn.utils.rnn.pad_packed_sequence.html#torch.nn.utils.rnn.pad_packed_sequence)
can be used to recover the underlying tensor packed in [`PackedSequence`](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence).

Note

This function accepts any input that has at least two dimensions. You
can apply it to pack the labels, and use the output of the RNN with
them to compute the loss directly. A Tensor can be retrieved from
a [`PackedSequence`](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence) object by accessing its `.data` attribute.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - padded batch of variable length sequences.
- **lengths** ([*Tensor*](../tensors.html#torch.Tensor)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*(*[*int*](https://docs.python.org/3/library/functions.html#int)*)*) - list of sequence lengths of each batch
element (must be on the CPU if provided as a tensor).
- **batch_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, the input is expected in `B x T x *`
format, `T x B x *` otherwise. Default: `False`.
- **enforce_sorted** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, the input is expected to
contain sequences sorted by length in a decreasing order. If
`False`, the input will get sorted unconditionally. Default: `True`.

Return type:

[*PackedSequence*](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence)

Warning

The dim of `input` tensor will be truncated if its length larger than
correspond value in `length`.

Returns:

a [`PackedSequence`](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence) object

Return type:

[*PackedSequence*](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence)