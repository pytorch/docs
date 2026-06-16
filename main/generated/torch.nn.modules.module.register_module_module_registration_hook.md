# torch.nn.modules.module.register_module_module_registration_hook

torch.nn.modules.module.register_module_module_registration_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/modules/module.py#L165)

Register a module registration hook common to all modules.

Warning

This adds global state to the nn.Module module

The hook will be called every time `register_module()` is invoked.
It should have the following signature:

```
hook(module, name, submodule) -> None or new submodule
```

The hook can modify the input or return a single modified value in the hook.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`