# torch.nn.utils.rnn.unpad_sequence

torch.nn.utils.rnn.unpad_sequence(*padded_sequences*, *lengths*, *batch_first=False*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/utils/rnn.py#L473)

Unpad padded Tensor into a list of variable length Tensors.

`unpad_sequence` unstacks padded Tensor into a list of variable length Tensors.

Example

```
>>> from torch.nn.utils.rnn import pad_sequence, unpad_sequence
>>> a = torch.ones(25, 300)
>>> b = torch.ones(22, 300)
>>> c = torch.ones(15, 300)
>>> sequences = [a, b, c]
>>> padded_sequences = pad_sequence(sequences)
>>> lengths = torch.as_tensor([v.size(0) for v in sequences])
>>> unpadded_sequences = unpad_sequence(padded_sequences, lengths)
>>> torch.allclose(sequences[0], unpadded_sequences[0])
True
>>> torch.allclose(sequences[1], unpadded_sequences[1])
True
>>> torch.allclose(sequences[2], unpadded_sequences[2])
True
```

Parameters:

- **padded_sequences** ([*Tensor*](../tensors.html#torch.Tensor)) - padded sequences.
- **lengths** ([*Tensor*](../tensors.html#torch.Tensor)) - length of original (unpadded) sequences.
- **batch_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether batch dimension first or not. Default: `False`.

Returns:

a list of `Tensor` objects

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Tensor*](../tensors.html#torch.Tensor)]