# StreamContext

*class*torch.cuda.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/__init__.py#L830)

Context-manager that selects a given stream.

All CUDA kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.