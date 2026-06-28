# torch.compiler.keep_tensor_guards_unsafe

torch.compiler.keep_tensor_guards_unsafe(*guard_entries*, *keep_parameters=False*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/compiler/__init__.py#L826)

A common function to keep tensor guards on all tensors. This is unsafe to
use by default. But if you don't expect any changes in the model code, you
can just keep the tensor guards.

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.keep_tensor_guards},
>> )