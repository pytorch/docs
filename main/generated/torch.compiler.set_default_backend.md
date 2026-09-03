# torch.compiler.set_default_backend

torch.compiler.set_default_backend(*backend*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/compiler/__init__.py#L356)

Set the default backend for `torch.compile` when no `backend` argument is specified.

Passing `None` resets the default back to `"inductor"`.

Parameters:

**backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**...**]**,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - A backend name (string), a callable backend, or `None`.

Example:

```
>>> torch.compiler.set_default_backend("eager")
>>> torch.compiler.get_default_backend()
'eager'
>>> torch.compiler.set_default_backend(None) # reset
>>> torch.compiler.get_default_backend()
'inductor'
```