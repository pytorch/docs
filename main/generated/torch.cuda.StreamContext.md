# StreamContext

*class*torch.cuda.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/__init__.py#L814)

Context-manager that selects a given stream.

All CUDA kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.