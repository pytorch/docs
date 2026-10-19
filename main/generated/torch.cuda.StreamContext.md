# StreamContext

*class*torch.cuda.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L908)

Context-manager that selects a given stream.

All CUDA kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.