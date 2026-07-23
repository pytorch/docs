# Graph

*class*torch.accelerator.Graph(*keep_graph=False*, ***, *pool=None*, *capture_error_mode='default'*)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L9)

Wrapper around an [accelerator](../torch.html#accelerators) graph that supports capture and replay.

A graph captures a sequence of operations and their dependencies, allowing them to be
replayed efficiently with reduced overhead. This class can be used as a context manager
to automatically capture operations on the current stream.

Parameters:

- **keep_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `False`, the underlying graph is destroyed and the
executable graph is instantiated on the GPU at the end of `capture_end`.
If `True`, the underlying graph is preserved after `capture_end`. In this case,
the executable graph is not instantiated automatically; it must be explicitly created
by calling `instantiate`, or it will be instantiated on the first call to `replay`.
Defaults to `False`.
- **pool** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Memory pool identifier for this graph. Multiple graphs
can share the same pool by passing the same identifier, which can reduce memory overhead.
Defaults to `None`.
- **capture_error_mode** (*Literal**[**"default"**,**"global"**,**"thread_local"**,**"relaxed"**]**,**optional*) - Specifies the behavior of graph capture. The exact semantics are backend-specific.
`"default"`: backend-defined default capture behavior.
`"global"`: potentially unsafe API calls are prohibited. Errors may occur if capture
in the current thread affects other threads.
`"thread_local"`: potentially unsafe API calls are prohibited. Errors occur only if
capture in the current thread affects itself.
`"relaxed"`: the current thread is allowed to make potentially unsafe API calls, except
for calls that inherently conflict with stream capture.
Default: `"default"`.

Return type:

*Self*

Example:

```
>>> x = torch.zeros([2000], device=0)

>>> stream = torch.Stream()
>>> graph = torch.accelerator.Graph()
>>> with stream, graph:
... x += 1

>>> graph.replay()
```

capture_begin()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L76)

Begin graph capture on the current stream.

All operations on the current stream after this call will be recorded into the graph until
`capture_end` is called, using the memory pool and capture error mode provided at construction time.

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L87)

End graph capture on the current stream of the current device.

After this call, the graph can be replayed via `replay`.

debug_dump(*path*)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L140)

Dump the captured graph to a file for debugging purposes if the debugging is
enabled via `enable_debug_mode`.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path to dump the graph to.

Example::

```
>>> s = torch.Stream()
>>> g = torch.accelerator.Graph()
>>> g.enable_debug_mode()
```

```
>>> with s, g:
>>> # ... operations ...
```

```
>>> # Dump captured graph to a file "graph_dump.dot"
>>> g.debug_dump("graph_dump.dot")
```

enable_debug_mode()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L136)

Enable debugging mode for `debug_dump`.

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L95)

Instantiate the underlying graph. Will be called by `capture_end`
if `keep_graph=False`, or by `replay` if `keep_graph=True` and
`instantiate` has not already been explicitly called.

pool()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L116)

Return an opaque token representing the id of this graph's memory pool.

This id can optionally be passed to another graph's `capture_begin`,
which hints the other graph may share the same memory pool.

Example::

```
>>> g1 = torch.accelerator.Graph()
>>> g1.capture_begin()
>>> # ... operations ...
>>> g1.capture_end()
```

```
>>> # Share g1's memory pool with a new graph
>>> pool_id = g1.pool()
>>> g2 = torch.accelerator.Graph(pool=pool_id)
```

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

replay()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L103)

Replay the work captured by this graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/accelerator/graphs.py#L107)

Delete the graph currently held by this instance.

After this call, the graph can be recaptured. Set `graph_pool` or
`capture_error_mode` beforehand to use different settings on the next capture.