# torch.compiler.load_compiled_function

torch.compiler.load_compiled_function(*file*, ***, *f_globals=None*, *external_data=None*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/compiler/__init__.py#L958)

Load an aot-compiled function from a file.

Warning

This API is currently experimental and subject to change.

Parameters:

- **file** ([*IOBase*](https://docs.python.org/3/library/io.html#io.IOBase)) - A file-like object containing the serialized compiled function.
- **f_globals** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*object*](https://docs.python.org/3/library/functions.html#object)*]**|**None*) - Optional global scope enclosing the compiled function.
- **external_data** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Optional data to be loaded into the runtime environment
of the compiled function. This should contain the same
data as AOTCompileResult.external_data returned from save_compiled_function() call.

Returns:

A torch-compiled function with compilation preloaded from disk.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]