# torch.optim.Optimizer.load_state_dict

Optimizer.load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/eeafed4de12b40ecc42bea4b9757d484a389d286/torch/optim/optimizer.py#L915)

Load the optimizer state.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)) - optimizer state. Should be an object returned
from a call to [`state_dict()`](torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict).

Warning

By default, state tensors other than `step` are currently cast to the
parameter dtype for floating-point parameters. In a future release,
the default will preserve their saved dtype in order to respect the
dtype in the checkpoint. However, this behavior will break use cases
that rely on the state being automatically cast to the parameter's
dtype, as many optimizer [`step()`](torch.optim.Optimizer.step.html#torch.optim.Optimizer.step) implementations do not support
mixed precision. We emit a `FutureWarning` when loading the checkpoint
changes a state tensor's dtype. Use [`torch.optim.preserve_state_dtype_on_load()`](../optim.html#torch.optim.preserve_state_dtype_on_load)
to select the desired behavior explicitly. In either case, state tensors
are moved to the parameter's device.

Note

When preserving dtypes, state tensors must be compatible with the
selected optimizer implementation for [`step()`](torch.optim.Optimizer.step.html#torch.optim.Optimizer.step). Use
[`torch.optim.preserve_state_dtype_on_load()`](../optim.html#torch.optim.preserve_state_dtype_on_load) with `False` to
retain automatic casting, or explicitly convert state tensors before
stepping, for example with [`register_load_state_dict_post_hook()`](torch.optim.Optimizer.register_load_state_dict_post_hook.html#torch.optim.Optimizer.register_load_state_dict_post_hook).

Warning

Make sure this method is called after initializing [`torch.optim.lr_scheduler.LRScheduler`](torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler),
as calling it beforehand will overwrite the loaded learning rates.

Note

The `step` tensor keeps its saved dtype and device unless the parameter
group is fused or capturable, which moves it to the parameter's device as
`torch.float32`. This behavior is independent of the dtype preservation
setting.

Note

The names of the parameters (if they exist under the "param_names" key of each param group
in [`state_dict()`](torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict)) will not affect the loading process.
To use the parameters' names for custom cases (such as when the parameters in the loaded state dict
differ from those initialized in the optimizer),
a custom `register_load_state_dict_pre_hook` should be implemented to adapt the loaded dict
accordingly.
If `param_names` exist in loaded state dict `param_groups` they will be saved and override
the current names, if present, in the optimizer state. If they do not exist in loaded state dict,
the optimizer `param_names` will remain unchanged.

Example

```
>>> optimizer = ... # initialized optimizer matching the saved state
>>> scheduler1 = torch.optim.lr_scheduler.LinearLR(
... optimizer,
... start_factor=0.1,
... end_factor=1,
... total_iters=20,
... )
>>> scheduler2 = torch.optim.lr_scheduler.CosineAnnealingLR(
... optimizer,
... T_max=80,
... eta_min=3e-5,
... )
>>> lr = torch.optim.lr_scheduler.SequentialLR(
... optimizer,
... schedulers=[scheduler1, scheduler2],
... milestones=[20],
... )
>>> lr.load_state_dict(torch.load("./save_seq.pt"))
>>> # now load the optimizer checkpoint after loading the LRScheduler
>>> optimizer.load_state_dict(torch.load("./save_optim.pt"))
```