# torch.set_deterministic_debug_mode

torch.set_deterministic_debug_mode(*debug_mode*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/__init__.py#L2009)

Sets the debug mode for deterministic operations.

Note

This is an alternative interface for
[`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms). Refer to that function's
documentation for details about affected operations.

Parameters:

**debug_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - If "default" or 0, don't error or warn on
nondeterministic operations. If "warn" or 1, warn on
nondeterministic operations. If "error" or 2, error on
nondeterministic operations.