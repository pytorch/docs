# torch.nn.utils.parametrize.remove_parametrizations

torch.nn.utils.parametrize.remove_parametrizations(*module*, *tensor_name*, *leave_parametrized=True*)[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/nn/utils/parametrize.py#L696)

Remove the parametrizations on a tensor in a module.

- If `leave_parametrized=True`, `module[tensor_name]` will be set to
its current output. In this case, the parametrization shall not change the `dtype`
of the tensor.
- If `leave_parametrized=False`, `module[tensor_name]` will be set to
the unparametrised tensor in `module.parametrizations[tensor_name].original`.
This is only possible when the parametrization depends on just one tensor.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module from which remove the parametrization
- **tensor_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - name of the parametrization to be removed
- **leave_parametrized** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - leave the attribute `tensor_name` parametrized.
Default: `True`

Returns:

module

Return type:

[Module](torch.nn.Module.html#torch.nn.Module)

Raises:

- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) - if `module[tensor_name]` is not parametrized
- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) - if `leave_parametrized=False` and the parametrization depends on several tensors