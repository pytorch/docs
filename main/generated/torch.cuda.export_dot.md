# torch.cuda.export_dot

torch.cuda.export_dot(*path*, ***, *verbose=True*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/graphs.py#L1127)

Return a capture-end hook that dumps the captured graph to `path` in
Graphviz DOT format. Register it with
[`CUDAGraph.register_capture_end_hook()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.register_capture_end_hook); works for both `keep_graph`
modes since it runs while the template is still live.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*CUDAGraph*](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph)], None]