# torch.fx.operator_schemas.normalize_function

torch.fx.operator_schemas.normalize_function(*target*, *args*, *kwargs=None*, *arg_types=None*, *kwarg_types=None*, *normalize_to_only_use_kwargs=False*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/fx/operator_schemas.py#L387)

Returns normalized arguments to PyTorch functions. This means that
args/kwargs will be matched up to the functional's
signature and return exclusively kwargs in positional order if
normalize_to_only_use_kwargs is True.
Also populates default values. Does not support positional-only
parameters or varargs parameters (`*args`, `**kwargs`). Does not support modules.

May require arg_types and kwarg_types in order to disambiguate overloads.

Parameters:

- **target** (*Callable*) - Function that we are normalizing
- **args** (*Tuple**[**Any**]*) - Tuple of args to the function
- **kwargs** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - Dict of kwargs to the function
- **arg_types** (*Optional**[**Tuple**[**Any**]**]*) - Tuple of arg types for the args
- **kwarg_types** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - Dict of arg types for the kwargs
- **normalize_to_only_use_kwargs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to normalize to only use kwargs.

Returns:

Returns normalized_args_and_kwargs, or None if not successful.

Return type:

*ArgsKwargsPair* | None

Warning

This API is experimental and is *NOT* backward-compatible.