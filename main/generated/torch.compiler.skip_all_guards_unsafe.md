# torch.compiler.skip_all_guards_unsafe

torch.compiler.skip_all_guards_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/compiler/__init__.py#L796)

A function for skipping all guards on a compiled function.

WARNING: This function will drop all the safety guarantees from Dynamo

compiled function. Use this with caution.

To use this API, use guard_filter_fn argument while calling torch.compile

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.skip_all_guards_unsafe},
>> )