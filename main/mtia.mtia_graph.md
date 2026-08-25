# torch.mtia.mtia_graph

The MTIA backend is implemented out of the tree, only interfaces are defined here.

torch.mtia.mtia_graph.graph_pool_handle()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L12)

Return an opaque token representing the id of a graph memory pool.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

*class*torch.mtia.mtia_graph.MTIAGraph(*keep_graph=False*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L20)

Wrapper around a MTIA graph.

Return type:

Self

capture_begin(*pool*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L28)

Begin capturing a MTIA graph.

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L34)

End the capture of a MTIA graph.

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L40)

Instantiate the captured MTIA graph.

pool()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L58)

Return an opaque token representing the id of this graph's memory pool

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

replay()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L46)

Replay the captured MTIA graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L52)

Destroy the captured graph and reset the states.

*class*torch.mtia.mtia_graph.graph(*mtia_graph*, *pool=None*, *stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/mtia/mtia_graph.py#L65)