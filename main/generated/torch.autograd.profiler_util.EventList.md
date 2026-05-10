# EventList

*class*torch.autograd.profiler_util.EventList(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/autograd/profiler_util.py#L29)

A list of profiling events with helper methods for analysis and visualization.

EventList extends the standard Python list to provide specialized methods for
working with profiling events (FunctionEvent or FunctionEventAvg objects).
It includes utilities for aggregating statistics, formatting output tables,
and exporting profiling data.

This class is typically returned by profiler methods and should not be
instantiated directly by users.

Parameters:

- ***args** - Standard list arguments.
- **use_device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Device type for profiling ("cuda", "xpu", etc.).
- **profile_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether memory profiling was enabled. Default: False.
- **with_flops** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to include FLOP counts. Default: False.

Variables:

- **_use_device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type being profiled.
- **_profile_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether memory profiling is enabled.
- **_with_flops** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether FLOP counting is enabled.
- **_tree_built** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether the event tree structure has been built.

Key Methods:

table(...): Format events as a table string for display.
export_chrome_trace(path): Export to Chrome tracing format.
export_stacks(path, metric): Export stack traces with metrics.
key_averages(...): Compute averaged statistics grouped by operation name.
total_average(): Compute aggregate totals across all events (sums, not averages).

Properties:

self_cpu_time_total: Sum of self CPU time across all events.

Example:

```
import torch
from torch.profiler import profile, ProfilerActivity

with profile(activities=[ProfilerActivity.CPU]) as prof:
 x = torch.randn(100, 100)
 y = torch.matmul(x, x)

# EventList is returned by prof.events()
events = prof.events()

# Display as formatted table
print(
 events.table(
 sort_by="cpu_time_total", row_limit=20, top_level_events_only=False
 )
)

# Export to Chrome tracing format
events.export_chrome_trace("trace.json")

# Get averaged statistics
avg_events = events.key_averages()
print(avg_events.table())

# Export stack traces
events.export_stacks("stacks.txt", "self_cpu_time_total")
```

See also

- [`FunctionEvent`](torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent): Individual profiling event
- [`FunctionEventAvg`](torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg): Averaged profiling statistics
- `table()`: Format events as a readable table
- `key_averages()`: Aggregate events by operation name

append(*object*, */*)

Append object to the end of the list.

clear()

Remove all items from list.

copy()

Return a shallow copy of the list.

count(*value*, */*)

Return number of occurrences of value.

export_chrome_trace(*path*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/autograd/profiler_util.py#L288)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.

extend(*iterable*, */*)

Extend list by appending elements from the iterable.

index(*value*, *start=0*, *stop=9223372036854775807*, */*)

Return first index of value.

Raises ValueError if the value is not present.

insert(*index*, *object*, */*)

Insert object before index.

key_averages(*group_by_input_shapes=False*, *group_by_stack_n=0*, *group_by_overload_name=False*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/autograd/profiler_util.py#L376)

Averages all function events over their keys.

Parameters:

- **group_by_input_shapes** - group entries by
(event name, input shapes) rather than just event name.
This is useful to see which input shapes contribute to the runtime
the most and may help with size-specific optimizations or
choosing the best candidates for quantization (aka fitting a roof line)
- **group_by_stack_n** - group by top n stack trace entries
- **group_by_overload_name** - Differentiate operators by their overload name e.g. aten::add.Tensor
- **separately** (*and aten::add.out will be aggregated*) -

Returns:

An EventList containing FunctionEventAvg objects.

pop(*index=-1*, */*)

Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

remove(*value*, */*)

Remove first occurrence of value.

Raises ValueError if the value is not present.

reverse()

Reverse *IN PLACE*.

sort(***, *key=None*, *reverse=False*)

Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

table(*sort_by=None*, *row_limit=100*, *max_src_column_width=75*, *max_name_column_width=55*, *max_shapes_column_width=80*, *header=None*, *top_level_events_only=False*, *time_unit=None*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/autograd/profiler_util.py#L242)

Print an EventList as a nicely formatted table.

Parameters:

- **sort_by** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Attribute used to sort entries. By default
they are printed in the same order as they were registered.
Valid keys include: `cpu_time`, `cuda_time`, `xpu_time`,
`cpu_time_total`, `cuda_time_total`, `xpu_time_total`,
`cpu_memory_usage`, `cuda_memory_usage`, `xpu_memory_usage`,
`self_cpu_memory_usage`, `self_cuda_memory_usage`,
`self_xpu_memory_usage`, `count`.
- **top_level_events_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Boolean flag to determine the
selection of events to display. If true, the profiler will only
display events at top level like top-level invocation of python
lstm, python add or other functions, nested events like low-level
cpu/cuda/xpu ops events are omitted for profiler result readability.
- **time_unit** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - A time unit to be used for all values in the
table. Valid options are: `s`, `ms` and `us`.

Returns:

A string containing the table.

total_average()[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/autograd/profiler_util.py#L444)

Compute aggregate statistics across all events.

Accumulates statistics from all events into a single FunctionEventAvg object.
This is primarily useful for computing total metrics (total CPU time, total
memory usage, etc.) across the entire profiling session, regardless of
operation type.

Note

This sums up times and counts across ALL different operations, so the
"average" metrics (like cpu_time) represent the average time per operation
call across the entire session, mixing all operation types together.
For per-operation averages, use `key_averages()` instead.

Returns:

A single aggregate object with key="Total" containing

accumulated statistics.

Return type:

[FunctionEventAvg](torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg)