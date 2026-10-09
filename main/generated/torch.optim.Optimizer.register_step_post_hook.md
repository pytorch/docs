# torch.optim.Optimizer.register_step_post_hook

Optimizer.register_step_post_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/optim/optimizer.py#L630)

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