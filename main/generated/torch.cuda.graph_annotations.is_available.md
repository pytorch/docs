# torch.cuda.graph_annotations.is_available

torch.cuda.graph_annotations.is_available() → [bool](https://docs.python.org/3/builtins/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/cuda/_graph_annotations.py#L366)

Return whether CUDA graph annotation recording is supported.

Requires a CUDA device, the `cuda-bindings` package, and a driver
that supports `cudaGraphNodeGetToolsId` (CUDA >= 13.1 or an
equivalent cuda-compat package). When this returns `False`,
[`mark_kernels()`](torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels) is a silent no-op and no annotations are
recorded.

The first call may probe the CUDA driver; the result is cached.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)