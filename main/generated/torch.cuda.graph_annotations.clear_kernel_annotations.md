# torch.cuda.graph_annotations.clear_kernel_annotations

torch.cuda.graph_annotations.clear_kernel_annotations() → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/cuda/_graph_annotations.py#L579)

Clear all recorded kernel annotations.

The annotation registry is process-global and accumulates across
captures; long-running workloads that capture many graphs should clear
it once recorded annotations have been consumed (e.g. after saving
them alongside a profiler trace).

Warning

This API is in prototype and may change in future releases.