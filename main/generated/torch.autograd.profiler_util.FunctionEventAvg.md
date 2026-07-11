# FunctionEventAvg

*class*torch.autograd.profiler_util.FunctionEventAvg[[source]](https://github.com/pytorch/pytorch/blob/e708521bdf92712674ed3a0d332b56c356502328/torch/autograd/profiler_util.py#L1008)

Averaged profiling statistics over multiple FunctionEvent objects.

FunctionEventAvg aggregates statistics from multiple FunctionEvent objects
with the same key (typically same operation name). This is useful for getting
average performance metrics across multiple invocations of the same operation.

This class is typically created by calling [`EventList.key_averages()`](torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList.key_averages) on
a profiler's event list.

Variables:

- **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Grouping key for the events (typically operation name).
- **count** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Total number of events aggregated.
- **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Node identifier for distributed profiling (-1 if not applicable).
- **is_async** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether the operations are asynchronous.
- **is_remote** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether the operations occurred on a remote node.
- **use_device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type being profiled ("cuda", "xpu", etc.).
- **cpu_time_total** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated total CPU time in microseconds.
- **device_time_total** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated total device time in microseconds.
- **self_cpu_time_total** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated self CPU time (excluding children) in microseconds.
- **self_device_time_total** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated self device time (excluding children) in microseconds.
- **input_shapes** (*List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - Input tensor shapes (requires record_shapes=true).
- **overload_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Operator overload name (requires _ExperimentalConfig(capture_overload_names=True) set).
- **stack** (*List**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - Python stack trace where the operation was called (requires with_stack=true).
- **scope** ([*int*](https://docs.python.org/3/library/functions.html#int)) - at::RecordScope identifier (0=forward, 1=backward, etc.).
- **cpu_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated CPU memory usage in bytes.
- **device_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated device memory usage in bytes.
- **self_cpu_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated self CPU memory usage in bytes.
- **self_device_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Accumulated self device memory usage in bytes.
- **cpu_children** (*List**[*[*FunctionEvent*](torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent)*]*) - CPU child events.
- **cpu_parent** ([*FunctionEvent*](torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent)) - CPU parent event.
- **device_type** (*DeviceType*) - Type of device (CPU, CUDA, XPU, PrivateUse1, etc.).
- **is_legacy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether from legacy profiler.
- **flops** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Total floating point operations.
- **is_user_annotation** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this is a user-annotated region.

Properties:

cpu_time (float): Average CPU time per invocation.
device_time (float): Average device time per invocation.

See also

- [`EventList.key_averages`](torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList.key_averages): Method that creates FunctionEventAvg objects
- [`FunctionEvent`](torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent): Individual profiling event
- [`EventList`](torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList): Container for profiling events