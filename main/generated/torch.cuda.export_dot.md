# torch.cuda.export_dot

torch.cuda.export_dot(*path*, ***, *verbose=True*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/cuda/graphs.py#L1127)

Return a capture-end hook that dumps the captured graph to `path` in
Graphviz DOT format. Register it with
[`CUDAGraph.register_capture_end_hook()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.register_capture_end_hook); works for both `keep_graph`
modes since it runs while the template is still live.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*CUDAGraph*](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph)], None]