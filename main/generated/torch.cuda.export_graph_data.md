# torch.cuda.export_graph_data

torch.cuda.export_graph_data(*path*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cuda/graphs.py#L745)

Return a post-instantiate hook that pickles [`CUDAGraph.get_graph_data()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.get_graph_data)
to `path`. Register it with [`CUDAGraph.register_post_instantiate_hook()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.register_post_instantiate_hook):
`get_graph_data` needs the graph instantiated (it remaps node ids to the
exec graph id), and at post-instantiate time the template is still live, so
this works for both `keep_graph` modes.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*CUDAGraph*](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph)], None]