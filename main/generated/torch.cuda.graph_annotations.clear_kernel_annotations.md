# torch.cuda.graph_annotations.clear_kernel_annotations

torch.cuda.graph_annotations.clear_kernel_annotations() → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/cuda/_graph_annotations.py#L560)

Clear all recorded kernel annotations.

The annotation registry is process-global and accumulates across
captures; long-running workloads that capture many graphs should clear
it once recorded annotations have been consumed (e.g. after saving
them alongside a profiler trace).

Warning

This API is in prototype and may change in future releases.