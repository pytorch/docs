# torch.nn.modules.module.register_module_forward_hook

torch.nn.modules.module.register_module_forward_hook(*hook*, ***, *with_kwargs=False*, *always_call=False*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/nn/modules/module.py#L249)

Register a global forward hook for all the modules.

Warning

This adds global state to the nn.module module
and it is only intended for debugging/profiling purposes.

The hook will be called every time after `forward()` has computed an output.
It should have the following signature:

```
hook(module, input, output) -> None or modified output
```

The input contains only the positional arguments given to the module.
Keyword arguments won't be passed to the hooks and only to the `forward`.
You can optionally modify the output of the module by returning a new value
that will replace the output from the `forward()` function.

Parameters:

- **hook** (*Callable*) - The user defined hook to be registered.
- **always_call** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` the `hook` will be run regardless of
whether an exception is raised while calling the Module.
Default: `False`

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

This hook will be executed before specific module hooks registered with
`register_forward_hook`.