# torch.fx.passes.infra.pass_manager.pass_result_wrapper

torch.fx.passes.infra.pass_manager.pass_result_wrapper(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/fx/passes/infra/pass_manager.py#L20)

Wrapper for passes which currently do not return a PassResult.
This wrapper makes them return a PassResult containing the modified object
and True for the "modified" flag.

Parameters:

**fn** (*Callable**[*[*Module*](torch.nn.Module.html#torch.nn.Module)*,**Any**]*) -

Returns:

wrapped_fn (Callable[Module, PassResult])

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], *PassResult* | None]

Warning

This API is experimental and is *NOT* backward-compatible.