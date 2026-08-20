# torch.cuda.graph_annotations.clear_kernel_annotations

torch.cuda.graph_annotations.clear_kernel_annotations() → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/_graph_annotations.py#L993)

Clear all recorded kernel annotations.

The annotation registry is process-global and accumulates across
captures; long-running workloads that capture many graphs should clear
it once recorded annotations have been consumed (e.g. after saving
them alongside a profiler trace).

Clearing forgets everything recorded so far and revokes recording from
every scope opened before the clear: backward hooks that
[`mark_kernels()`](torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels) attached to existing autograd nodes stay on the
graph but become inert. Scopes opened after the clear record normally.

Warning

This API is in prototype and may change in future releases.