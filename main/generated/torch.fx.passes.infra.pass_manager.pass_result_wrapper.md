# torch.fx.passes.infra.pass_manager.pass_result_wrapper

torch.fx.passes.infra.pass_manager.pass_result_wrapper(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/fx/passes/infra/pass_manager.py#L20)

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