# torch.optim.Optimizer.register_step_post_hook

Optimizer.register_step_post_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/optim/optimizer.py#L622)

Register an optimizer step post hook which will be called after optimizer step.

It should have the following signature:

```
hook(optimizer, args, kwargs) -> None
```

The `optimizer` argument is the optimizer instance being used.

Parameters:

**hook** (*Callable*) - The user defined hook to be registered.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`