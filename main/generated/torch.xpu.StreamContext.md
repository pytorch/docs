# StreamContext

*class*torch.xpu.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/xpu/__init__.py#L591)

Context-manager that selects a given stream.

All XPU kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.