# torch.cuda.graph_annotations.dump_kernel_py_stacks

torch.cuda.graph_annotations.dump_kernel_py_stacks(*path*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/_graph_annotations.py#L1322)

Save recorded CUDA graph launch stacks as gzip-compressed JSON.

The file maps decimal node-id strings to the stack strings described by
[`get_kernel_py_stacks()`](torch.cuda.graph_annotations.get_kernel_py_stacks.html#torch.cuda.graph_annotations.get_kernel_py_stacks).
Call after instantiation and before resetting or destroying the graphs.

Parameters:

**path** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Output file path.

Warning

This API is in prototype and may change in future releases.