# torch.mps.profiler.start

torch.mps.profiler.start(*mode='interval'*, *wait_until_completed=False*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/mps/profiler.py#L21)

Start OS Signpost tracing from MPS backend.

The generated OS Signposts could be recorded and viewed in
XCode Instruments Logging tool.

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