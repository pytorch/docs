# torch.cuda.comm.scatter

torch.cuda.comm.scatter(*tensor*, *devices=None*, *chunk_sizes=None*, *dim=0*, *streams=None*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/nn/parallel/comm.py#L171)

Scatters tensor across multiple GPUs.

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor to scatter. Can be on CPU or GPU.
- **devices** (*Iterable**[*[*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - an iterable of
GPU devices, among which to scatter.
- **chunk_sizes** (*Iterable**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - sizes of chunks to be placed on
each device. It should match `devices` in length and sums to
`tensor.size(dim)`. If not specified, `tensor` will be divided
into equal chunks.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - A dimension along which to chunk `tensor`.
Default: `0`.
- **streams** (*Iterable**[*[*torch.cuda.Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)*]**,**optional*) - an iterable of Streams, among
which to execute the scatter. If not specified, the default stream will
be utilized.
- **out** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*]**,**optional**,**keyword-only*) - the GPU tensors to
store output results. Sizes of these tensors must match that of
`tensor`, except for `dim`, where the total size must
sum to `tensor.size(dim)`.

Note

Exactly one of `devices` and `out` must be specified. When
`out` is specified, `chunk_sizes` must not be specified and
will be inferred from sizes of `out`.

Returns:

- If `devices` is specified,

a tuple containing chunks of `tensor`, placed on
`devices`.
- If `out` is specified,

a tuple containing `out` tensors, each containing a chunk of
`tensor`.