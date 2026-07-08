# torch.compiler.keep_portable_guards_unsafe

torch.compiler.keep_portable_guards_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/compiler/__init__.py#L763)

A common function to only keep guards that can be used in both Python and non-Python environments.
This includes:
- Tensor metadata and dynamic shape information.
- Global contexts state (e.g. autocast, no_grad, etc.)

This is unsafe to use by default.
To use this API, use guard_filter_fn argument while calling torch.compile

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.keep_global_context_and_tensor_guards_unsafe},
>> )