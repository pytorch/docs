# torch.compiler.keep_tensor_guards_unsafe

torch.compiler.keep_tensor_guards_unsafe(*guard_entries*, *keep_parameters=False*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/compiler/__init__.py#L859)

A common function to keep tensor guards on all tensors. This is unsafe to
use by default. But if you don't expect any changes in the model code, you
can just keep the tensor guards.

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.keep_tensor_guards},
>> )