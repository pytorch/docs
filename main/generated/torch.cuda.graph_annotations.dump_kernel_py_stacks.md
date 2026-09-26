# torch.cuda.graph_annotations.dump_kernel_py_stacks

torch.cuda.graph_annotations.dump_kernel_py_stacks(*path*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/_graph_annotations.py#L1322)

Save recorded CUDA graph launch stacks as gzip-compressed JSON.

The file maps decimal node-id strings to the stack strings described by
[`get_kernel_py_stacks()`](torch.cuda.graph_annotations.get_kernel_py_stacks.html#torch.cuda.graph_annotations.get_kernel_py_stacks).
Call after instantiation and before resetting or destroying the graphs.

Parameters:

**path** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Output file path.

Warning

This API is in prototype and may change in future releases.