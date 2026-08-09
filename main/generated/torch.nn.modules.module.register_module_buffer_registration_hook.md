# torch.nn.modules.module.register_module_buffer_registration_hook

torch.nn.modules.module.register_module_buffer_registration_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/nn/modules/module.py#L139)

Register a buffer registration hook common to all modules.

Warning

This adds global state to the nn.Module module

The hook will be called every time `register_buffer()` is invoked.
It should have the following signature:

```
hook(module, name, buffer) -> None or new buffer
```

The hook can modify the input or return a single modified value in the hook.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`