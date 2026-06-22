# torch.profiler

## Overview

PyTorch Profiler is a tool that allows the collection of performance metrics during training and inference.
Profiler's context manager API can be used to better understand what model operators are the most expensive,
examine their input shapes and stack traces, study device kernel activity and visualize the execution trace.

Note

An earlier version of the API in [`torch.autograd`](autograd.html#module-torch.autograd) module is considered legacy and will be deprecated.

torch.profiler.profiler.schedule(***, *wait*, *warmup*, *active*, *repeat=0*, *skip_first=0*, *skip_first_wait=0*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L667)

Returns a callable that can be used as profiler `schedule` argument. The profiler will skip
the first `skip_first` steps, then wait for `wait` steps, then do the warmup for the next `warmup` steps,
then do the active recording for the next `active` steps and then repeat the cycle starting with `wait` steps.
The optional number of cycles is specified with the `repeat` parameter, the zero value means that
the cycles will continue until the profiling is finished.

The `skip_first_wait` parameter controls whether the first `wait` stage should be skipped.
This can be useful if a user wants to wait longer than `skip_first` between cycles, but not
for the first profile. For example, if `skip_first` is 10 and `wait` is 20, the first cycle will
wait 10 + 20 = 30 steps before warmup if `skip_first_wait` is zero, but will wait only 10
steps if `skip_first_wait` is non-zero. All subsequent cycles will then wait 20 steps between the
last active and warmup.

Return type:

Callable

torch.profiler.profiler.supported_activities()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L92)

Returns a set of supported profiler tracing activities.

Note: profiler uses CUPTI library to trace on-device CUDA kernels.
In case when CUDA is enabled but CUPTI is not available, passing
`ProfilerActivity.CUDA` to profiler results in using the legacy CUDA
profiling code (same as in the legacy `torch.autograd.profiler`).
This, in turn, results in including CUDA time in the profiler table output,
but not in the JSON trace.

torch.profiler.profiler.tensorboard_trace_handler(*dir_name*, *worker_name=None*, *use_gzip=False*, *use_python_export=False*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L737)

Outputs tracing files to directory of `dir_name`, then that directory can be
directly delivered to tensorboard as logdir.
`worker_name` should be unique for each worker in distributed scenario,
it will be set to '[hostname]_[pid]' by default.

## API Reference

*class*torch.profiler.profile(***, *activities=None*, *schedule=None*, *on_trace_ready=None*, *record_shapes=False*, *profile_memory=False*, *with_stack=False*, *with_flops=False*, *with_modules=False*, *experimental_config=None*, *execution_trace_observer=None*, *acc_events=False*, *use_cuda=None*, *custom_trace_id_callback=None*, *post_processing_timeout_s=None*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L773)

Profiler context manager.

Parameters:

- **activities** (*iterable*) -

list of activity groups (CPU, CUDA) to use in profiling, supported values:
`torch.profiler.ProfilerActivity.CPU`, `torch.profiler.ProfilerActivity.CUDA`,
`torch.profiler.ProfilerActivity.XPU`.
Default value: ProfilerActivity.CPU and (when available) ProfilerActivity.CUDA
or (when available) ProfilerActivity.XPU.

Each item can be a `ProfilerActivity` enum (collects all default
activity types for that group) or a `dict` mapping a `ProfilerActivity`
to a list of individual activity type names to collect, e.g.
`{ProfilerActivity.CUDA: ["GPU_MEMCPY", "CUDA_RUNTIME"]}`.
An empty list (e.g. `{ProfilerActivity.CUDA: []}`) means collect
nothing for that group.
The same activity group must not appear more than once.
- **schedule** (*Callable*) - callable that takes step (int) as a single parameter and returns
`ProfilerAction` value that specifies the profiler action to perform at each step.
- **on_trace_ready** (*Callable*) - callable invoked at the end of each profiling cycle
(when `schedule` returns `ProfilerAction.RECORD_AND_SAVE`). Receives the
`profile` instance as its only argument, typically used to export the
trace (e.g. via `export_chrome_trace()`) or print a summary.
- **record_shapes** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - save information about operator's input shapes.
- **profile_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - track tensor memory allocation/deallocation.
- **with_stack** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - record source information (file and line number) for the ops.
- **with_flops** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - use formula to estimate the FLOPs (floating point operations) of specific operators
(matrix multiplication and 2D convolution).
- **with_modules** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - record module hierarchy (including function names)
corresponding to the callstack of the op. e.g. If module A's forward call's
module B's forward which contains an aten::add op,
then aten::add's module hierarchy is A.B
Note that this support exist, at the moment, only for TorchScript models
and not eager mode models.
- **experimental_config** (*_ExperimentalConfig*) - A set of experimental options
used for Kineto library features. Note, backward compatibility is not guaranteed.
- **execution_trace_observer** (*ExecutionTraceObserver*) - A PyTorch Execution Trace Observer object.
[PyTorch Execution Traces](https://arxiv.org/pdf/2305.14516.pdf) offer a graph based
representation of AI/ML workloads and enable replay benchmarks, simulators, and emulators.
When this argument is included the observer start() and stop() will be called for the
same time window as PyTorch profiler. See the examples section below for a code sample.
- **acc_events** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Enable the accumulation of FunctionEvents across multiple profiling cycles
- **post_processing_timeout_s** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Optional timeout in seconds for post-processing profiler
results. If specified, event parsing will stop after this duration and return partial
results. Useful for handling large traces that may take too long to process.
- **custom_trace_id_callback** (*Callable**[**[**]**,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**,**optional*) - User-supplied trace ID generator,
invoked once per profiling cycle. Defaults to a random UUID; retrieve via
`get_trace_id()`.
- **use_cuda** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) -

Deprecated since version 1.8.1: use `activities` instead.

Note

Use `schedule()` to generate the callable schedule.
Non-default schedules are useful when profiling long training jobs
and allow the user to obtain multiple traces at the different iterations
of the training process.
The default schedule simply records all the events continuously for the
duration of the context manager.

Note

Use `tensorboard_trace_handler()` to generate result files for TensorBoard:

`on_trace_ready=torch.profiler.tensorboard_trace_handler(dir_name)`

After profiling, result files can be found in the specified directory. Use the command:

`tensorboard --logdir dir_name`

to see the results in TensorBoard.
For more information, see
[PyTorch Profiler TensorBoard Plugin](https://github.com/pytorch/kineto/tree/master/tb_plugin)

Note

Enabling shape and stack tracing results in additional overhead.
When record_shapes=True is specified, profiler will temporarily hold references to the tensors;
that may further prevent certain optimizations that depend on the reference count and introduce
extra tensor copies.

Examples:

```
with torch.profiler.profile(
 activities=[
 torch.profiler.ProfilerActivity.CPU,
 torch.profiler.ProfilerActivity.CUDA,
 ]
) as p:
 code_to_profile()
print(p.key_averages().table(sort_by="self_cuda_time_total", row_limit=-1))
```

Using the profiler's `schedule`, `on_trace_ready` and `step` functions:

```
# Non-default profiler schedule allows user to turn profiler on and off
# on different iterations of the training loop;
# trace_handler is called every time a new trace becomes available
def trace_handler(prof):
 print(
 prof.key_averages().table(sort_by="self_cuda_time_total", row_limit=-1)
 )
 # prof.export_chrome_trace("/tmp/test_trace_" + str(prof.step_num) + ".json")

with torch.profiler.profile(
 activities=[
 torch.profiler.ProfilerActivity.CPU,
 torch.profiler.ProfilerActivity.CUDA,
 ],
 # In this example with wait=1, warmup=1, active=2, repeat=1,
 # profiler will skip the first step/iteration,
 # start warming up on the second, record
 # the third and the fourth iterations,
 # after which the trace will become available
 # and on_trace_ready (when set) is called;
 # the cycle repeats starting with the next step
 schedule=torch.profiler.schedule(wait=1, warmup=1, active=2, repeat=1),
 on_trace_ready=trace_handler,
 # on_trace_ready=torch.profiler.tensorboard_trace_handler('./log')
 # used when outputting for tensorboard
) as p:
 for iter in range(N):
 code_iteration_to_profile(iter)
 # send a signal to the profiler that the next iteration has started
 p.step()
```

The following sample shows how to setup up an Execution Trace Observer (execution_trace_observer)

```
with torch.profiler.profile(
 ...
 execution_trace_observer=(
 ExecutionTraceObserver().register_callback("./execution_trace.json")
 ),
) as p:
 for iter in range(N):
 code_iteration_to_profile(iter)
 p.step()
```

You can also refer to test_execution_trace_with_kineto() in tests/profiler/test_profiler.py.
Note: One can also pass any object satisfying the _ITraceObserver interface.

add_metadata(*key*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L529)

Adds a user defined metadata with a string key and a string value
into the trace file

add_metadata_json(*key*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L538)

Adds a user defined metadata with a string key and a valid json value
into the trace file

events()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L515)

Return the list of unaggregated [`FunctionEvent`](generated/torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent)
objects, for use in the trace callback or after profiling has finished.

export_chrome_trace(*path*, *use_python_export=False*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L409)

Exports the collected trace in Chrome JSON format. If kineto is enabled, only
last cycle in schedule is exported.

export_memory_timeline(*path*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L586)

Export memory event information from the profiler collected
tree for a given device, and export a timeline plot. There are 3
exportable files using `export_memory_timeline`, each controlled by the
`path`'s suffix.

- For an HTML compatible plot, use the suffix `.html`, and a memory timeline
plot will be embedded as a PNG file in the HTML file.
- For plot points consisting of `[times, [sizes by category]]`, where
`times` are timestamps and `sizes` are memory usage for each category.
The memory timeline plot will be saved a JSON (`.json`) or gzipped JSON
(`.json.gz`) depending on the suffix.
- For raw memory points, use the suffix `.raw.json.gz`. Each raw memory
event will consist of `(timestamp, action, numbytes, category)`, where
`action` is one of `[PREEXISTING, CREATE, INCREMENT_VERSION, DESTROY]`,
and `category` is one of the enums from
`torch.profiler._memory_profiler.Category`.

Output: Memory timeline written as gzipped JSON, JSON, or HTML.

Deprecated since version ``export_memory_timeline``: is deprecated and will be removed in a future version.
Please use `torch.cuda.memory._record_memory_history` and
`torch.cuda.memory._export_memory_snapshot` instead.

export_stacks(*path*, *metric='self_cpu_time_total'*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L448)

Save stack traces to a file

Parameters:

- **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - save stacks file to this location;
- **metric** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - metric to use: "self_cpu_time_total" or "self_cuda_time_total"

get_trace_id()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L1246)

Returns the current trace ID.

key_averages(*group_by_input_shape=False*, *group_by_stack_n=0*, *group_by_overload_name=False*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L492)

Averages events, grouping them by operator name and (optionally) input shapes, stack
and overload name.

Returns an [`EventList`](generated/torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList) of the aggregated events.

Note

To use shape/stack functionality make sure to set record_shapes/with_stack
when creating profiler context manager.

preset_metadata_json(*key*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L546)

Preset a user defined metadata when the profiler is not started
and added into the trace file later.
Metadata is in the format of a string key and a valid json value

set_custom_trace_id_callback(*callback*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L1239)

Set the trace ID generator. Called at the start of each cycle, so updating
it between cycles yields distinct IDs per cycle.

step()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L1150)

Signals the profiler that the next profiling step has started.

toggle_collection_dynamic(*enable*, *activities*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L459)

Toggle collection of activities on/off at any point of collection. Currently supports toggling Torch Ops
(CPU) and CUDA activity supported in Kineto

Parameters:

**activities** (*iterable*) - list of activity groups to use in profiling, supported values:
`torch.profiler.ProfilerActivity.CPU`, `torch.profiler.ProfilerActivity.CUDA`

Examples:

```
with torch.profiler.profile(
 activities=[
 torch.profiler.ProfilerActivity.CPU,
 torch.profiler.ProfilerActivity.CUDA,
 ]
) as p:
 code_to_profile_0()
 // turn off collection of all CUDA activity
 p.toggle_collection_dynamic(False, [torch.profiler.ProfilerActivity.CUDA])
 code_to_profile_1()
 // turn on collection of all CUDA activity
 p.toggle_collection_dynamic(True, [torch.profiler.ProfilerActivity.CUDA])
 code_to_profile_2()
print(p.key_averages().table(
 sort_by="self_cuda_time_total", row_limit=-1))
```

*class*torch.profiler.ProfilerAction(*value*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/profiler.py#L644)

Profiler actions that can be taken at the specified intervals.

NONE, WARMUP, RECORD, and RECORD_AND_SAVE are user-facing values that may
be returned from a user-provided schedule. DEVICE_STOPPED is set
internally by the profiler when device collection stops early due to
errors; it must not be returned from a user-provided schedule.

*class*torch.profiler.ProfilerActivity

Members:

CPU

XPU

MTIA

CUDA

HPU

PrivateUse1

*property*name

## Intel Instrumentation and Tracing Technology APIs

torch.profiler.itt.is_available()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/itt.py#L31)

Check if ITT feature is available or not

torch.profiler.itt.mark(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/itt.py#L57)

Describe an instantaneous event that occurred at some point.

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with the event.

torch.profiler.itt.range_push(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/itt.py#L38)

Pushes a range onto a stack of nested range span. Returns zero-based
depth of the range that is started.

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with range

torch.profiler.itt.range_pop()[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/itt.py#L49)

Pops a range off of a stack of nested range spans. Returns the
zero-based depth of the range that is ended.

torch.profiler.itt.range(*msg*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/profiler/itt.py#L67)

Context manager / decorator that pushes an ITT range at the beginning
of its scope, and pops it at the end. If extra arguments are given,
they are passed as arguments to msg.format().

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - message to associate with the range

 This module needs to be documented. Adding here in the meantime
for tracking purposes