# torch.cuda.set_sync_debug_mode

torch.cuda.set_sync_debug_mode(*debug_mode*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/cuda/__init__.py#L1305)

Set the debug mode for cuda synchronizing operations.

Parameters:

**debug_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - if "default" or 0, don't error or warn on synchronizing operations,
if "warn" or 1, warn on synchronizing operations, if "error" or 2, error out synchronizing operations.

Warning

This is an experimental feature, and not all synchronizing operations will trigger warning or error. In
particular, operations in torch.distributed and torch.sparse namespaces are not covered yet.