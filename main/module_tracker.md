# torch.utils.module_tracker

This utility can be used to track the current position inside an [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module) hierarchy.
It can be used within other tracking tools to be able to easily associate measured quantities to user-friendly names. This is used in particular in the FlopCounterMode today.

*class*torch.utils.module_tracker.ModuleTracker[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/utils/module_tracker.py#L25)

`ModuleTracker` is a context manager that tracks the nn.Module hierarchy during execution
so that other system can query which Module is currently being executed (or its backward is being
executed).

You can access the `parents` attribute on this context manager to get the set of all the
Modules currently being executed via their fqn (fully qualified name, also used as the key within
the state_dict).
You can access the `is_bw` attribute to know if you are currently running in backward or not.

Note that `parents` is never empty and always contains the "Global" key. The `is_bw` flag
will remain `True` after the forward until another Module is executed. If you need it to be
more accurate, please submit an issue requesting this. Adding a map from fqn to the module instance
is possible but not done yet, please submit an issue requesting this if you need it.

Example usage

```
mod = torch.nn.Linear(2, 2)

with ModuleTracker() as tracker:
 # Access anything during the forward pass
 def my_linear(m1, m2, bias):
 print(f"Current modules: {tracker.parents}")
 return torch.mm(m1, m2.t()) + bias

 torch.nn.functional.linear = my_linear

 mod(torch.rand(2, 2))
```