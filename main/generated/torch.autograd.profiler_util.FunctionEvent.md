# FunctionEvent

*class*torch.autograd.profiler_util.FunctionEvent(*id*, *name*, *thread*, *start_us*, *end_us*, *overload_name=None*, *fwd_thread=None*, *input_shapes=None*, *stack=None*, *scope=0*, *use_device=None*, *cpu_memory_usage=0*, *device_memory_usage=0*, *is_async=False*, *is_remote=False*, *sequence_nr=-1*, *node_id=-1*, *device_type=<DeviceType.CPU: 0>*, *device_index=0*, *device_resource_id=None*, *is_legacy=False*, *flops=None*, *trace_name=None*, *concrete_inputs=None*, *kwinputs=None*, *is_user_annotation=False*, *is_python_function=False*, *activity_type=None*, *metadata_json=None*, *flow_id=None*, *flow_type=None*, *flow_start=None*, *external_id=0*, *linked_correlation_id=0*, *extra_meta=None*, *structured_input_shapes=None*, *structured_input_strides=None*, *input_dtypes=None*, *python_id=-1*, *python_parent_id=-1*, *python_module_id=-1*, *typed_metadata=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/autograd/profiler_util.py#L668)

Profiling information about a single function.

FunctionEvent records the execution of a single operation during profiling.
These events are obtained from the profiler/kineto and contain detailed
timing and memory usage information.

Note

FunctionEvent objects are typically created by the profiler/kineto and should not
be instantiated directly by users. Access them through the profiler's output.

Variables:

- **id** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Unique identifier for this event.
- **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Node identifier for distributed profiling (-1 if not applicable).
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the profiled function/operator.
- **overload_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Overload name for the operator (requires _ExperimentalConfig(capture_overload_names=True) set).
- **trace_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Same as name, just changes ProfilerStep* to ProfilerStep#
- **time_range** ([*Interval*](torch.autograd.profiler_util.Interval.html#torch.autograd.profiler_util.Interval)) - Time interval containing start and end timestamps in microseconds.
- **thread** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Thread ID where the operation started.
- **fwd_thread** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Thread ID of the corresponding forward operation.
- **kernels** (*List**[*[*Kernel*](torch.autograd.profiler_util.Kernel.html#torch.autograd.profiler_util.Kernel)*]*) - List of device kernels launched by this operation.
- **count** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of times this event was called (usually 1).
- **cpu_children** (*List**[**FunctionEvent**]*) - Direct CPU child operations.
- **cpu_parent** (*FunctionEvent*) - Direct CPU parent operation.
- **input_shapes** (*List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - Shapes of input tensors (requires record_shapes=True).
For plain tensor inputs, each entry is a list of dimensions (e.g. `[16, 16]`).
TensorList inputs are represented as an empty list `[]`; use
`structured_input_shapes` to get per-element shapes for TensorList inputs.
- **concrete_inputs** (*List**[**Any**]*) - Concrete input values (requires record_shapes=true).
- **kwinputs** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]*) - Keyword arguments (requires record_shapes=true).
- **stack** (*List**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - Python stack trace where the operation was called (requires with_stack=true).
- **scope** ([*int*](https://docs.python.org/3/library/functions.html#int)) - at::RecordScope identifier (0=forward, 1=backward, etc.).
- **use_device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type being profiled ("cuda", "xpu", etc.).
- **cpu_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - CPU memory allocated in bytes.
- **device_memory_usage** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Device memory allocated in bytes.
- **is_async** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this is an asynchronous operation.
- **is_remote** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this operation occurred on a remote node.
- **sequence_nr** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Sequence number for autograd operations.
- **device_type** (*DeviceType*) - Type of device (CPU, CUDA, XPU, PrivateUse1, etc.).
- **device_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Index of the device (e.g., GPU 0, 1, 2).
- **device_resource_id** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Resource ID on the device (ie. stream ID).
- **is_legacy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this is from the legacy profiler.
- **flops** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Estimated floating point operations.
- **is_user_annotation** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this is a user-annotated region.
- **metadata** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]*) - Additional metadata keyed by the field names
used in exported traces. Use
`_ExperimentalConfig(expose_kineto_event_metadata=True)` to expose
Kineto activity metadata. Available fields vary by activity and backend.
- **metadata_json** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Deprecated. Use event_metadata instead.
- **event_metadata** (*EventMetadata*) - Additional metadata in structured format.
- **structured_input_shapes** (*List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]**]*) - Like `input_shapes`
but distinguishes TensorList inputs. Plain tensor inputs are `List[int]`;
TensorList inputs are `List[List[int]]` containing one shape per tensor in the list.
Matches the `"Input Dims"` field in the Chrome trace JSON.
- **structured_input_strides** (*List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]**]*) - Strides of input
tensors in the same format as `structured_input_shapes` (requires
record_shapes=True).

Properties:

cpu_time_total (float): Total CPU time in microseconds.
device_time_total (float): Total device (CUDA/XPU/etc) time in microseconds.
self_cpu_time_total (float): CPU time excluding child operations.
self_device_time_total (float): Device time excluding child operations.
self_cpu_memory_usage (int): CPU memory usage excluding child operations.
self_device_memory_usage (int): Device memory usage excluding child operations.
cpu_time (float): Average CPU time per call.
device_time (float): Average device time per call.
key (str): Key used for grouping events (usually same as name).

See also

- [`torch.profiler.profile`](../profiler.html#torch.profiler.profile): Context manager for profiling
- [`EventList`](torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList): List container for FunctionEvent objects with helper methods
- [`FunctionEventAvg`](torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg): Averaged statistics over multiple FunctionEvent objects

append_cpu_child(*child*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/autograd/profiler_util.py#L855)

Append a CPU child of type FunctionEvent.

One is supposed to append only direct children to the event to have
correct self cpu time being reported.

set_cpu_parent(*parent*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/autograd/profiler_util.py#L869)

Set the immediate CPU parent of type FunctionEvent.

One profiling FunctionEvent should have only one CPU parent such that
the child's range interval is completely inside the parent's. We use
this connection to determine the event is from top-level op or not.