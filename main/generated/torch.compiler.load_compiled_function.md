# torch.compiler.load_compiled_function

torch.compiler.load_compiled_function(*file*, ***, *f_globals=None*, *external_data=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/compiler/__init__.py#L1003)

Load an aot-compiled function from a file.

Warning

This API is currently experimental and subject to change.

When `f_globals` is passed and a global is itself the source of a kept
guard, the returned callable re-reads that global from it before every call,
so it is not safe to share between threads that rebind such a global
concurrently, with or without the GIL; load the artifact once per thread
instead.

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
guards check on the next call. The compiled bytecode reads a
load-time snapshot of this dict merged over the globals
serialized with the artifact, so a name this dict omits
still resolves there; on top of that, a global that is
itself the source of a kept guard is re-read from this dict
on every call, so a rebind the guards ACCEPT - a
same-metadata swap under a kept `TENSOR_MATCH`, which
checks metadata, not values - is what the call computes
with, and a store the compiled function itself makes to
such a global does not carry over to its next call. A
global that is not itself a kept guard's source keeps its
load-time value - one only a symbolic-shape guard reads
included - and so does a container a guard reaches only
through a sub-path such as `D['a']`, whose other members
nothing certifies: a rebind of either is not seen, even
when the guard on `D['a']` passes. The re-read is not
atomic with the guard check before it, and it writes into
the loaded callable's own globals, shared by every call of
it; the user guide covers both.
- **external_data** ([*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Optional data to be loaded into the runtime environment
of the compiled function. This should contain the same
data as AOTCompileResult.external_data returned from save_compiled_function() call.

Returns:

A torch-compiled function with compilation preloaded from disk.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]