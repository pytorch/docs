# torch.nn.modules.module.register_module_module_registration_hook

torch.nn.modules.module.register_module_module_registration_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/modules/module.py#L165)

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