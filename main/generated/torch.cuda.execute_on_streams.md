# torch.cuda.execute_on_streams

torch.cuda.execute_on_streams(*streams*, *fn*, **inputs*)[[source]](https://github.com/pytorch/pytorch/blob/3d5976e3f87222f326a3b2c424828b74ec6cf594/torch/cuda/streams.py#L283)

Enqueue a callback on each stream and join its work to the caller stream.

Calls `fn(*args)` for corresponding items from the input sequences, with
each stream made current in order. Returns the results in the same order.
Python callbacks run sequentially; their CUDA work may execute concurrently.
Each stream waits for work previously submitted to the caller's current
stream. Subsequent work on the caller stream waits for every callback's
queued work, including work queued before a callback raises. These waits
do not synchronize the host.

The caller's current stream and device are restored on success or failure.
After a callback raises, remaining callbacks are not invoked. Callbacks
must enqueue their work on the supplied stream or join other work to it.

Streams may belong to different devices. Keep the tensors and any owning
green contexts alive until their work completes; normal cross-stream
tensor lifetime rules still apply.

Parameters:

- **streams** (*Sequence**[*[*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)*]*) - Nonempty sequence of ordinary or green-context CUDA streams.
- **fn** (*Callable**[**...**,**_T**]*) - Callback receiving one item from each input sequence.
- ***inputs** (*Sequence**[**Any**]*) - One or more sequences, each with one item per stream.

Returns:

List of callback results in stream order.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[_T]