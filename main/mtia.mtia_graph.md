# torch.mtia.mtia_graph

The MTIA backend is implemented out of the tree, only interfaces are defined here.

torch.mtia.mtia_graph.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L12)

Return whether MTIA graph capture is underway on the current stream.

If an MTIA context does not exist on the current device, return `False`
without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.mtia.mtia_graph.graph_pool_handle()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L21)

Return an opaque token representing the id of a graph memory pool.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

*class*torch.mtia.mtia_graph.MTIAGraph(*keep_graph=False*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L29)

Wrapper around a MTIA graph.

Return type:

Self

capture_begin(*pool*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L37)

Begin capturing a MTIA graph.

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L43)

End the capture of a MTIA graph.

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L49)

Instantiate the captured MTIA graph.

pool()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L67)

Return an opaque token representing the id of this graph's memory pool

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

replay()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L55)

Replay the captured MTIA graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L61)

Destroy the captured graph and reset the states.

*class*torch.mtia.mtia_graph.graph(*mtia_graph*, *pool=None*, *stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/mtia/mtia_graph.py#L74)