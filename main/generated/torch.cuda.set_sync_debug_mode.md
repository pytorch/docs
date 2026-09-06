# torch.cuda.set_sync_debug_mode

torch.cuda.set_sync_debug_mode(*debug_mode*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/cuda/__init__.py#L1438)

Set the debug mode for cuda synchronizing operations.

Parameters:

**debug_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - if "default" or 0, don't error or warn on synchronizing operations,
if "warn" or 1, warn on synchronizing operations, if "error" or 2, error out synchronizing operations.

Warning

This is an experimental feature, and not all synchronizing operations will trigger warning or error. In
particular, operations in torch.distributed and torch.sparse namespaces are not covered yet.