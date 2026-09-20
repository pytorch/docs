# torch.mps.profiler.profile

torch.mps.profiler.profile(*mode='interval'*, *wait_until_completed=False*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/mps/profiler.py#L52)

Context Manager to enabling generating OS Signpost tracing from MPS backend.

Parameters:

- **mode** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - OS Signpost tracing mode could be "interval", "event",
or both "interval,event".
The interval mode traces the duration of execution of the operations,
whereas event mode marks the completion of executions.
See document [Recording Performance Data](https://developer.apple.com/documentation/os/logging/recording_performance_data) for more info.
- **wait_until_completed** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Waits until the MPS Stream complete
executing each encoded GPU operation. This helps generating single
dispatches on the trace's timeline.
Note that enabling this option would affect the performance negatively.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[None]