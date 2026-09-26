# torch.cuda.graph_annotations.get_kernel_py_stacks

torch.cuda.graph_annotations.get_kernel_py_stacks()[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/_graph_annotations.py#L1295)

Return Python launch stacks recorded during CUDA graph capture.

Enable recording with `torch.cuda.graph(..., enable_annotations=True,
annotation_config={"record_py_stacks": True})`. Values contain user launch
frames as newline-separated `filename:line:function` strings, innermost
first. Framework and generated Inductor frames are omitted by default;
`annotation_config["py_stack_filter_paths"]` can replace the excluded
directories, or disable filtering with an empty list.

With the default `key_by="exec"`, match a Cuspy Chrome trace event using
`(args["graph id"] << 32) | args["graph node id"]`. For consumers reading
CUPTI's `sourceGraphNodeId`, set `annotation_config["key_by"]="source"`
and use that ID directly (requires CUPTI and driver >= 13.4).
Conditional/child-body stacks require `"source"` keying; they are omitted
with `"exec"`.

The mapping is a live, read-only view. Save it with
[`dump_kernel_py_stacks()`](torch.cuda.graph_annotations.dump_kernel_py_stacks.html#torch.cuda.graph_annotations.dump_kernel_py_stacks) after instantiation and before resetting or
destroying the graph, which removes its entries.

Warning

This API is in prototype and may change in future releases.

Return type:

[*Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[int](https://docs.python.org/3/builtins/functions.html#int), [str](https://docs.python.org/3/builtins/stdtypes.html#str)]