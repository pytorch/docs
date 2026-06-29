# torch.utils.mobile_optimizer

PyTorch Mobile is no longer actively supported. Redirecting to [ExecuTorch documentation](https://docs.pytorch.org/executorch).

Warning

PyTorch Mobile is no longer actively supported. Please check out
[ExecuTorch](https://pytorch.org/executorch-overview), PyTorch's
all-new on-device inference library. You can also review
documentation on [XNNPACK](https://pytorch.org/executorch/stable/native-delegates-executorch-xnnpack-delegate.html)
and [Vulkan](https://pytorch.org/executorch/stable/native-delegates-executorch-vulkan-delegate.html) delegates.

torch.utils.mobile_optimizer.optimize_for_mobile(*script_module*, *optimization_blocklist=None*, *preserved_methods=None*, *backend='CPU'*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/utils/mobile_optimizer.py#L15)

Optimize a torch script module for mobile deployment.

Parameters:

- **script_module** (*ScriptModule*) - An instance of torch script module with type of ScriptModule.
- **optimization_blocklist** ([*set*](https://docs.python.org/3/library/stdtypes.html#set)*[**_MobileOptimizerType**]**|**None*) - A set with type of MobileOptimizerType. When set is not passed,
optimization method will run all the optimizer pass; otherwise, optimizer
method will run the optimization pass that is not included inside optimization_blocklist.
- **preserved_methods** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**AnyStr**]**|**None*) - A list of methods that needed to be preserved when freeze_module pass is invoked
- **backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type to use for running the result model ('CPU'(default), 'Vulkan' or 'Metal').

Returns:

A new optimized torch script module

Return type:

*RecursiveScriptModule*

torch.utils.mobile_optimizer.generate_mobile_module_lints(*script_module*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/utils/mobile_optimizer.py#L76)

Generate a list of lints for a given torch script module.

Parameters:

**script_module** (*ScriptModule*) - An instance of torch script module with type of ScriptModule.

Returns:

A list of dictionary that contains modules lints

Return type:

lint_map