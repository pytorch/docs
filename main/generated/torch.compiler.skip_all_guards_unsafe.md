# torch.compiler.skip_all_guards_unsafe

torch.compiler.skip_all_guards_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/compiler/__init__.py#L796)

A function for skipping all guards on a compiled function.

WARNING: This function will drop all the safety guarantees from Dynamo

compiled function. Use this with caution.

To use this API, use guard_filter_fn argument while calling torch.compile

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.skip_all_guards_unsafe},
>> )