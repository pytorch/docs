# torch.fx.passes.pass_manager.inplace_wrapper

torch.fx.passes.pass_manager.inplace_wrapper(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/fx/passes/pass_manager.py#L27)

Convenience wrapper for passes which modify an object inplace. This
wrapper makes them return the modified object instead.

Parameters:

**fn** (*Callable**[**Object**,**Any**]*) -

Returns:

wrapped_fn (Callable[Object, Object])

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Concatenate*](https://docs.python.org/3/library/typing.html#typing.Concatenate)[*_T*, ~_P]], *_T*]