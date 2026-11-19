# torch.compiler.skip_guard_on_globals_unsafe

torch.compiler.skip_guard_on_globals_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/a4a15a72064ca010a723eae7c73835fe206f8de6/torch/compiler/__init__.py#L925)

A common function to skip guards on all globals. This is unsafe to use by
default. But if you don't expect any changes in the globals, you can just
keep the tensor guards.

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.skip_guard_on_globals},
>> )