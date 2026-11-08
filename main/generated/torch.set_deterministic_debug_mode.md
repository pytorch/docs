# torch.set_deterministic_debug_mode

torch.set_deterministic_debug_mode(*debug_mode*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/__init__.py#L1943)

Sets the debug mode for deterministic operations.

Note

This is an alternative interface for
[`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms). Refer to that function's
documentation for details about affected operations.

Parameters:

**debug_mode** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - If "default" or 0, don't error or warn on
nondeterministic operations. If "warn" or 1, warn on
nondeterministic operations. If "error" or 2, error on
nondeterministic operations.