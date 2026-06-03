# torch.fx.operator_schemas.normalize_module

torch.fx.operator_schemas.normalize_module(*root*, *target*, *args*, *kwargs=None*, *normalize_to_only_use_kwargs=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/operator_schemas.py#L527)

Returns normalized arguments to PyTorch modules. This means that
args/kwargs will be matched up to the functional's
signature and return exclusively kwargs in positional order if
normalize_to_only_use_kwargs is True.
Also populates default values. Does not support positional-only
parameters or varargs parameters (`*args`, `**kwargs`).

Parameters:

- **root** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - root module upon which we query modules
- **target** (*Callable*) - Function that we are normalizing
- **args** (*Tuple**[**Any**]*) - Tuple of args to the function
- **kwargs** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - Dict of kwargs to the function
- **normalize_to_only_use_kwargs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to normalize to only use kwargs.

Returns:

Returns normalized_args_and_kwargs, or None if not successful.

Return type:

*ArgsKwargsPair* | None

Warning

This API is experimental and is *NOT* backward-compatible.