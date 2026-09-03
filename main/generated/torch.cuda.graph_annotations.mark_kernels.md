# torch.cuda.graph_annotations.mark_kernels

torch.cuda.graph_annotations.mark_kernels(*annotation*, ***, *backward=True*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/cuda/_graph_annotations.py#L798)

Context manager that annotates GPU work captured within its scope.

Must be used inside an active [`torch.cuda.graph`](torch.cuda.graph.html#torch.cuda.graph) capture with
`enable_annotations=True`. Every kernel, memcpy, and memset node the
capture adds within the scope is tagged with `annotation`. Outside
a capture, with annotations disabled, or when [`is_available()`](torch.cuda.graph_annotations.is_available.html#torch.cuda.graph_annotations.is_available) is
`False`, the context manager is a no-op.

When scopes overlap on the same node (e.g. nested scopes), their
annotation dicts are merged key-by-key with the inner scope winning
common keys.

By default backward work is annotated too: autograd nodes created by
forward operations inside the scope get hooks (via
[`torch.autograd.graph.node_creation_hook`](../autograd.html#torch.autograd.graph.node_creation_hook)) that bracket their
backward execution, so when the backward pass is itself captured -
in the same capture as the forward or in a later one - its kernels
are tagged with the same annotation, plus an `"autograd_phase":
"backward"` key marking them as backward work (`"autograd_phase"`
is therefore reserved: backward annotation overwrites it). When
backward runs outside a capture the hooks are a no-op. Ownership
extends to higher-order gradients: nodes created while a hooked node
executes (`create_graph=True`, checkpoint recomputation) inherit its
annotations, so a later grad-of-grad capture is attributed too.
`AccumulateGrad` nodes are never annotated: a leaf's node is created
once and cached, so scope ownership would be an accident of first use.
Pass `backward=False` to annotate only the forward work, e.g. when a
wrapper implements its own backward attribution. The keyword's
presence also serves as the feature probe for that native backward
support: `"backward" in inspect.signature(mark_kernels).parameters`.

Implementation: on entry, records the current stream's capture frontier
and its existing direct dependents; on scope exit, walks only the
dependent nodes added since entry (falling back to newly created graph
roots when the scope is the first captured work).

Parameters:

- **annotation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Metadata to attach to each captured node.
A string `s` is recorded as `{"name": s}`. Dict values must
be picklable. The key `"name"` names the region in trace
tooling; `"stream"` is reserved for stream-lane assignment.
- **backward** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to also annotate the backward kernels of
autograd nodes created inside the scope. Default: `True`.

Note

The nodes to annotate must be reachable from the capture frontier of
the stream that is current on scope entry. Work on a different
already-capturing stream must be synchronized with the current
stream first.

Note

Child-graph and conditional nodes have bodies in a separate
`cudaGraph_t` that this walk does not descend into, so their work is
left unannotated and a warning is issued. Descending is possible
(`cudaGraphNodeGetParams` exposes the body graphs), but would not be
enough on its own: a body's nodes are numbered in that graph's id space
and are renumbered again when the exec graph inlines them, and nothing
exposes that renumbering, so `remap_to_exec_graph()` could not key
the annotations to what a profiler reports. For the same reason a scope
*inside* a conditional body (`torch.cond` / `torch.while_loop`)
records nothing at all.

Warning

This API is in prototype and may change in future releases.

Example:

```
>>> g = torch.cuda.CUDAGraph()
>>> x = torch.randn(8, device="cuda")
>>> with torch.cuda.graph(g, enable_annotations=True):
... with torch.cuda.graph_annotations.mark_kernels("phase_A"):
... y = x + 1
```