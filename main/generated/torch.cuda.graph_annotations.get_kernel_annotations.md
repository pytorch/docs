# torch.cuda.graph_annotations.get_kernel_annotations

torch.cuda.graph_annotations.get_kernel_annotations() → Mapping[[int](https://docs.python.org/3/library/functions.html#int), [list](https://docs.python.org/3/library/stdtypes.html#list)][[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/_graph_annotations.py#L530)

Return the live registry of recorded kernel annotations.

Keys are opaque integers matching the `graph node id` field that
CUPTI-based profilers attach to kernel events; values are the lists of
annotation dicts recorded for that node. The registry accumulates
across captures and is global to the process.

The returned mapping is a **live view**: it is updated in place when a
graph is instantiated (annotation keys are rekeyed to the executable
graph's ids), so a reference obtained early stays current. Keys are
valid for joining against a profiler trace once the corresponding
graphs have been instantiated. Treat the mapping as read-only; snapshot
it with `dict(...)` if isolation is needed.

Warning

This API is in prototype and may change in future releases.

Example:

```
>>> annotations = torch.cuda.graph_annotations.get_kernel_annotations()
>>> with open("annotations.pkl", "wb") as f:
... pickle.dump(dict(annotations), f)
```

Return type:

Mapping[[int](https://docs.python.org/3/library/functions.html#int), [list](https://docs.python.org/3/library/stdtypes.html#list)[Any]]