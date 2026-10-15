# torch.compiler.skip_all_guards_unsafe

torch.compiler.skip_all_guards_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/compiler/__init__.py#L902)

A function for skipping all guards on a compiled function.

WARNING: This function will drop all the safety guarantees from Dynamo

compiled function. Use this with caution.

To use this API, use guard_filter_fn argument while calling torch.compile

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.skip_all_guards_unsafe},
>> )