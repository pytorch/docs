# torch.cuda.export_dot

torch.cuda.export_dot(*path*, ***, *verbose=True*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/graphs.py#L1055)

Return a capture-end hook that dumps the captured graph to `path` in
Graphviz DOT format. Register it with
[`CUDAGraph.register_capture_end_hook()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.register_capture_end_hook); works for both `keep_graph`
modes since it runs while the template is still live.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*CUDAGraph*](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph)], None]