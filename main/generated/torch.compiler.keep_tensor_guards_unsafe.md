# torch.compiler.keep_tensor_guards_unsafe

torch.compiler.keep_tensor_guards_unsafe(*guard_entries*, *keep_parameters=False*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/compiler/__init__.py#L754)

A common function to keep tensor guards on all tensors. This is unsafe to
use by default. But if you don't expect any changes in the model code, you
can just keep the tensor guards.

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.keep_tensor_guards},
>> )