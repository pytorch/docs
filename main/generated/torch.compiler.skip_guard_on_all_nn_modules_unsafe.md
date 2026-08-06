# torch.compiler.skip_guard_on_all_nn_modules_unsafe

torch.compiler.skip_guard_on_all_nn_modules_unsafe(*guard_entries*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/compiler/__init__.py#L838)

A common function to skip guards on all nn modules, both user defined as
well inbuilt nn modules (like torch.nn.Linear). This is unsafe to use by
default. But for majority of torch.compile users, the model code does not
modify the nn module attributes. They can benefit from reduction in guard
latency overhead using this API.

To use this API, use guard_filter_fn argument while calling torch.compile

>> opt_mod = torch.compile(
>> mod,
>> options={"guard_filter_fn": torch.compiler.skip_guard_on_all_nn_modules_unsafe},
>> )