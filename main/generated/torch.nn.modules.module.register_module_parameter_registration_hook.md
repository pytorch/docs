# torch.nn.modules.module.register_module_parameter_registration_hook

torch.nn.modules.module.register_module_parameter_registration_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/nn/modules/module.py#L191)

Register a parameter registration hook common to all modules.

Warning

This adds global state to the nn.Module module

The hook will be called every time `register_parameter()` is invoked.
It should have the following signature:

```
hook(module, name, param) -> None or new parameter
```

The hook can modify the input or return a single modified value in the hook.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`