# StreamContext

*class*torch.mtia.StreamContext(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/mtia/__init__.py#L318)

Context-manager that selects a given stream.

All MTIA kernels queued within its context will be enqueued on a selected
stream.

Parameters:

**Stream** ([*Stream*](torch.mtia.Stream_class.html#torch.mtia.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Note

Streams are per-device.