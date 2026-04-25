# Stream

*class*torch.Stream(*device*, ***, *priority*)

An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order.
It can control or synchronize the execution of other Stream or block the current host thread to ensure
the correct task sequencing. It supports with statement as a context manager to ensure the operators
within the with block are running on the corresponding stream.

See in-depth description of the CUDA behavior at [CUDA semantics](../notes/cuda.html#cuda-semantics) for details
on the exact semantic that applies to all devices.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device for the Stream.
If not given, the current [accelerator](../torch.html#accelerators) type will be used.
- **priority** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - priority of the stream, should be 0 or negative, where negative
numbers indicate higher priority. By default, streams have priority 0.

Returns:

An torch.Stream object.

Return type:

Stream

Example:

```
>>> with torch.Stream(device='cuda') as s_cuda:
>>> a = torch.randn(10, 5, device='cuda')
>>> b = torch.randn(5, 10, device='cuda')
>>> c = torch.mm(a, b)
```

is_capturing() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return true if this stream is currently recording work for graph capture.

Returns:

A boolean indicating if the stream is capturing.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> s_cuda.is_capturing()
```

query() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> s_cuda.query()
True
```

record_event(*event*) → [Event](torch.Event.html#torch.Event)

Record an event. En-queuing it into the Stream to allow further synchronization from the current point in the FIFO queue.

Parameters:

**event** ([`torch.Event`](torch.Event.html#torch.Event), optional) - event to record. If not given, a new one will be allocated.

Returns:

Recorded event.

Return type:

[Event](torch.Event.html#torch.Event)

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> e_cuda = s_cuda.record_event()
```

synchronize() → [None](https://docs.python.org/3/library/constants.html#None)

Wait for all the kernels in this stream to complete.

Example:

```
>>> s_cuda = torch.Stream(device='cuda')
>>> s_cuda.synchronize()
```

wait_event(*event*) → [None](https://docs.python.org/3/library/constants.html#None)

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([`torch.Event`](torch.Event.html#torch.Event)) - an event to wait for.

Example:

```
>>> s1_cuda = torch.Stream(device='cuda')
>>> s2_cuda = torch.Stream(device='cuda')
>>> e_cuda = s1_cuda.record_event()
>>> s2_cuda.wait_event(e_cuda)
```

wait_stream(*stream*) → [None](https://docs.python.org/3/library/constants.html#None)

Synchronize with another stream. All future work submitted to this stream will wait until all kernels
already submitted to the given stream are completed.

Parameters:

**stream** (`torch.Stream`) - a stream to synchronize.

Example:

```
>>> s1_cuda = torch.Stream(device='cuda')
>>> s2_cuda = torch.Stream(device='cuda')
>>> s2_cuda.wait_stream(s1_cuda)
```