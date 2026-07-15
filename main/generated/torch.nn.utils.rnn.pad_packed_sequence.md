# torch.nn.utils.rnn.pad_packed_sequence

torch.nn.utils.rnn.pad_packed_sequence(*sequence*, *batch_first=False*, *padding_value=0.0*, *total_length=None*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/utils/rnn.py#L327)

Pad a packed batch of variable length sequences.

It is an inverse operation to [`pack_padded_sequence()`](torch.nn.utils.rnn.pack_padded_sequence.html#torch.nn.utils.rnn.pack_padded_sequence).

The returned Tensor's data will be of size `T x B x *` (if `batch_first` is `False`)
or `B x T x *` (if `batch_first` is `True`) , where `T` is the length of the longest
sequence and `B` is the batch size.

Example

```
>>> from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
>>> seq = torch.tensor([[1, 2, 0], [3, 0, 0], [4, 5, 6]])
>>> lens = [2, 1, 3]
>>> packed = pack_padded_sequence(
... seq, lens, batch_first=True, enforce_sorted=False
... )
>>> packed
PackedSequence(data=tensor([4, 1, 3, 5, 2, 6]), batch_sizes=tensor([3, 2, 1]),
 sorted_indices=tensor([2, 0, 1]), unsorted_indices=tensor([1, 2, 0]))
>>> seq_unpacked, lens_unpacked = pad_packed_sequence(packed, batch_first=True)
>>> seq_unpacked
tensor([[1, 2, 0],
 [3, 0, 0],
 [4, 5, 6]])
>>> lens_unpacked
tensor([2, 1, 3])
```

Note

`total_length` is useful to implement the
`pack sequence -> recurrent network -> unpack sequence` pattern in a
[`Module`](torch.nn.Module.html#torch.nn.Module) wrapped in [`DataParallel`](torch.nn.DataParallel.html#torch.nn.DataParallel).
See [this FAQ section](../notes/faq.html#pack-rnn-unpack-with-data-parallelism) for
details.

Parameters:

- **sequence** ([*PackedSequence*](torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence)) - batch to pad
- **batch_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, the output will be in `B x T x *`
format, `T x B x *` otherwise.
- **padding_value** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - values for padded elements.
- **total_length** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - if not `None`, the output will be padded to
have length `total_length`. This method will throw [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
if `total_length` is less than the max sequence length in
`sequence`.

Returns:

Tuple of Tensor containing the padded sequence, and a Tensor
containing the list of lengths of each sequence in the batch.
Batch elements will be re-ordered as they were ordered originally when
the batch was passed to `pack_padded_sequence` or `pack_sequence`.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor)]