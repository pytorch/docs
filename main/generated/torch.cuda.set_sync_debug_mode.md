# torch.cuda.set_sync_debug_mode

torch.cuda.set_sync_debug_mode(*debug_mode*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/__init__.py#L1299)

Set the debug mode for cuda synchronizing operations.

Parameters:

**debug_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - if "default" or 0, don't error or warn on synchronizing operations,
if "warn" or 1, warn on synchronizing operations, if "error" or 2, error out synchronizing operations.

Warning

This is an experimental feature, and not all synchronizing operations will trigger warning or error. In
particular, operations in torch.distributed and torch.sparse namespaces are not covered yet.