# StreamContext

*class*torch.xpu.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/xpu/__init__.py#L604)

Context-manager that selects a given stream.

All XPU kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.