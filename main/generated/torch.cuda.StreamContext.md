# StreamContext

*class*torch.cuda.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/cuda/__init__.py#L908)

Context-manager that selects a given stream.

All CUDA kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.