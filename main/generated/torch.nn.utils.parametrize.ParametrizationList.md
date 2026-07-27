# ParametrizationList

*class*torch.nn.utils.parametrize.ParametrizationList(*modules*, *original*, *unsafe=False*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/nn/utils/parametrize.py#L95)

A sequential container that holds and manages the original parameters or buffers of a parametrized [`torch.nn.Module`](torch.nn.Module.html#torch.nn.Module).

It is the type of `module.parametrizations[tensor_name]` when `module[tensor_name]`
has been parametrized with [`register_parametrization()`](torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization).

If the first registered parametrization has a `right_inverse` that returns one tensor or
does not have a `right_inverse` (in which case we assume that `right_inverse` is the identity),
it will hold the tensor under the name `original`.
If it has a `right_inverse` that returns more than one tensor, these will be registered as
`original0`, `original1`, ...

Warning

This class is used internally by [`register_parametrization()`](torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization). It is documented
here for completeness. It shall not be instantiated by the user.

Parameters:

- **modules** (*sequence*) - sequence of modules representing the parametrizations
- **original** ([*Parameter*](torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter)*or*[*Tensor*](../tensors.html#torch.Tensor)) - parameter or buffer that is parametrized
- **unsafe** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean flag that denotes whether the parametrization
may change the dtype and shape of the tensor. Default: False
Warning: the parametrization is not checked for consistency upon registration.
Enable this flag at your own risk.

right_inverse(*value*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/nn/utils/parametrize.py#L255)

Call the `right_inverse` methods of the parametrizations in the inverse registration order.

Then, it stores the result in `self.original` if `right_inverse` outputs one tensor
or in `self.original0`, `self.original1`, ... if it outputs several.

Parameters:

**value** ([*Tensor*](../tensors.html#torch.Tensor)) - Value to which initialize the module