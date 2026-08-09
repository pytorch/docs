# torch.cuda.graph_annotations.clear_kernel_annotations

torch.cuda.graph_annotations.clear_kernel_annotations() → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/cuda/_graph_annotations.py#L686)

Clear all recorded kernel annotations.

The annotation registry is process-global and accumulates across
captures; long-running workloads that capture many graphs should clear
it once recorded annotations have been consumed (e.g. after saving
them alongside a profiler trace).

Warning

This API is in prototype and may change in future releases.