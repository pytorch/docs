# Event

*class*torch.Event(*device=None*, ***, *enable_timing=False*, *blocking=False*, *interprocess=False*)

Query and record Stream status to identify or control dependencies across Stream and measure timing.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device for the Event.
If not given, the current [accelerator](../torch.html#accelerators) type will be used.
- **enable_timing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should measure time (default: `False`)
- **blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, [`wait()`](torch.wait.html#torch.wait) will be blocking (default: `False`)
- **interprocess** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, the event can be shared between processes (default: `False`)

Warning

Both blocking and interprocess are not supported right now and are noops.

Returns:

An torch.Event object.

Return type:

Event

Example:

```
>>> event = torch.Event()
>>> e_cuda = torch.Event(device='cuda')
```

elapsed_time(*end_event*) → [float](https://docs.python.org/3/library/functions.html#float)

Returns the elapsed time in milliseconds between when this event and the `end_event` are
each recorded via [`torch.Stream.record_event()`](torch.Stream.html#torch.Stream.record_event).

Parameters:

**end_event** (`torch.Event`) - The ending event has been recorded.

Returns:

Time between starting and ending event in milliseconds.

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> e1_cuda = s_cuda.record_event()
>>> e2_cuda = s_cuda.record_event()
>>> ms = e1_cuda.elapsed_time(e2_cuda)
```

query() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if the stream where this event was recorded already moved past the point where the event was recorded.
Always returns `True` if the Event was not recorded.

Returns:

A boolean indicating if all work currently captured by event has completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> e_cuda = s_cuda.record_event()
>>> e_cuda.query()
True
```

record(*stream=None*) → [None](https://docs.python.org/3/library/constants.html#None)

Record the event in a given stream. The stream's device must match the event's device.
This function is equivalent to `stream.record_event(self)`.

Parameters:

**stream** ([`torch.Stream`](torch.Stream.html#torch.Stream), optional) - A stream to be recorded.
If not given, the current stream will be used.

Example:

```
>>> e_cuda = torch.Event(device='cuda')
>>> e_cuda.record()
```

synchronize() → [None](https://docs.python.org/3/library/constants.html#None)

Wait for the event to complete. This prevents the CPU thread from proceeding until the event completes.

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> e_cuda = s_cuda.record_event()
>>> e_cuda.synchronize()
```

wait(*stream=None*) → [None](https://docs.python.org/3/library/constants.html#None)

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([`torch.Stream`](torch.Stream.html#torch.Stream), optional) - A stream to synchronize.
If not given, the current stream will be used.

Example:

```
>>> s1_cuda = torch.Stream(device='cuda')
>>> s2_cuda = torch.Stream(device='cuda')
>>> e_cuda = s1_cuda.record()
>>> e_cuda.wait(s2)
```