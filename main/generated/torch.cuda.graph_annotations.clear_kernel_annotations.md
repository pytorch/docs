# torch.cuda.graph_annotations.clear_kernel_annotations

torch.cuda.graph_annotations.clear_kernel_annotations() → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/cuda/_graph_annotations.py#L1115)

Clear all recorded kernel annotations.

Deprecated since version 2.15: The registry is self-bounding, so nothing needs to call this. Annotations are
rekeyed to the exec graph id on instantiation and dropped when that graph is
destroyed; in a long-running workload - where graphs are captured once and
replayed for the whole run - a global wipe instead discards annotations for
graphs that are still live and still being joined against.

Forgets everything recorded so far. It does not stop anything from recording:
the backward hooks [`mark_kernels()`](torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels) attached to live autograd nodes cannot be
detached and go on writing into the emptied registry, and a forward scope open
across the clear registers on exit as usual. In particular this breaks backward
projection across a forward/backward capture pair - the forward graph's entries
are gone and its scope no longer names the backward graph's kernels.

Warning

This API is in prototype and may change in future releases.