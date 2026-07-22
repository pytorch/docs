# torch.autograd.profiler.profile.total_average

profile.total_average()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/autograd/profiler.py#L1021)

Compute aggregate statistics across all events.

Accumulates statistics from all events into a single FunctionEventAvg object.
This is primarily useful for computing total metrics (total CPU time, total
memory usage, etc.) across the entire profiling session, regardless of
operation type.

Note

This sums up times and counts across ALL different operations, so the
"average" metrics (like cpu_time) represent the average time per operation
call across the entire session, mixing all operation types together.
For per-operation averages, use [`key_averages()`](torch.autograd.profiler.profile.key_averages.html#torch.autograd.profiler.profile.key_averages) instead.

Returns:

A single aggregate object with key="Total" containing

accumulated statistics.

Return type:

[FunctionEventAvg](torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg)