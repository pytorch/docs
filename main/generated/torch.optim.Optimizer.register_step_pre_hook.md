# torch.optim.Optimizer.register_step_pre_hook

Optimizer.register_step_pre_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/optim/optimizer.py#L607)

Register an optimizer step pre hook which will be called before optimizer step.

It should have the following signature:

```
hook(optimizer, args, kwargs) -> None or modified args and kwargs
```

The `optimizer` argument is the optimizer instance being used. If
args and kwargs are modified by the pre-hook, then the transformed
values are returned as a tuple containing the new_args and new_kwargs.

Parameters:

**hook** (*Callable*) - The user defined hook to be registered.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`