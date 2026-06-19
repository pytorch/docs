# torch.mps.profiler.profile

torch.mps.profiler.profile(*mode='interval'*, *wait_until_completed=False*)[[source]](https://github.com/pytorch/pytorch/blob/de1ad93d5279bade131efce3de7f798aef4faa3d/torch/mps/profiler.py#L52)

Context Manager to enabling generating OS Signpost tracing from MPS backend.

Parameters:

- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - OS Signpost tracing mode could be "interval", "event",
or both "interval,event".
The interval mode traces the duration of execution of the operations,
whereas event mode marks the completion of executions.
See document [Recording Performance Data](https://developer.apple.com/documentation/os/logging/recording_performance_data) for more info.
- **wait_until_completed** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Waits until the MPS Stream complete
executing each encoded GPU operation. This helps generating single
dispatches on the trace's timeline.
Note that enabling this option would affect the performance negatively.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[None]