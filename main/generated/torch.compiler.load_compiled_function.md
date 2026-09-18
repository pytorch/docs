# torch.compiler.load_compiled_function

torch.compiler.load_compiled_function(*file*, ***, *f_globals=None*, *external_data=None*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/compiler/__init__.py#L1006)

Load an aot-compiled function from a file.

Warning

This API is currently experimental and subject to change.

Parameters:

- **file** ([*IOBase*](https://docs.python.org/3/library/io.html#io.IOBase)) - A file-like object containing the serialized compiled function.
- **f_globals** ([*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*object*](https://docs.python.org/3/builtins/functions.html#object)*]**|**None*) - Optional live global scope enclosing the compiled function,
and the scope its kept guards resolve globals against,
symbolic-shape guards included: whether one installs as a
Python lambda (the default) or as a C++ guard under
`enable_cpp_symbolic_shape_guards`, its global operands
resolve here. When a kept guard reads a global - which,
beyond a symbolic-shape guard on a global with a dynamic
dim, takes a `guard_filter_fn` that keeps global guards,
since the default drops them all - pass `vars(mod)` for
the module `mod` that DEFINED the original function rather
than a dict of a few extra names: every global a kept guard
reads has to be bound here with a value that satisfies it,
or else the call raises `RuntimeError: GuardManager check
failed` rather than recompiling. Under the default filter
no other kept guard reads a global, so this dict only widens
what the bytecode merges over (below) with nothing checking
it; pass only the names the load cannot otherwise resolve,
if any. Passing `{}` is
an empty guard scope, not the same as omitting the argument,
which resolves the guards against the scope rebuilt from the
artifact instead. The
dict is held by reference and written into: the load may
add the Dynamo-generated globals a kept guard is rooted at,
and `__builtins__` when it has to build the builtins dict
one of those names holds, never overwriting a key it already
binds, and a global rebound in it afterwards is what the
guards check on the next call. The compiled bytecode instead
reads a load-time snapshot of this dict merged over the
globals serialized with the artifact, so a name this dict
omits still resolves there and a rebind the guards ACCEPT
leaves the call computing with the load-time value - a known
limitation rather than a contract to rely on.
- **external_data** ([*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Optional data to be loaded into the runtime environment
of the compiled function. This should contain the same
data as AOTCompileResult.external_data returned from save_compiled_function() call.

Returns:

A torch-compiled function with compilation preloaded from disk.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]