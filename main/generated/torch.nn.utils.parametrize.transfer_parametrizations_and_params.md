# torch.nn.utils.parametrize.transfer_parametrizations_and_params

torch.nn.utils.parametrize.transfer_parametrizations_and_params(*from_module*, *to_module*, *tensor_name=None*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/nn/utils/parametrize.py#L811)

Transfer parametrizations and the parameters they parametrize from `from_module` to `to_module`.

If `tensor_name` is specified, only transfers the specified parameter, otherwise
transfers all parametrized parameters. If those parameters do not exist in to_module, it will create them.
Does nothing if from_module is not parametrized.

Parameters:

- **from_module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module to transfer from
- **to_module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module to transfer to
- **tensor_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - parameter to transfer

Returns:

to_module

Return type:

[Module](torch.nn.Module.html#torch.nn.Module)