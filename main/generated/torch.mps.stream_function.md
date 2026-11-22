# torch.mps.stream

torch.mps.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/mps/streams.py#L66)

Context manager that selects a given stream.

MPS operators called within this context will be enqueued on the selected
stream.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This manager is a no-op if it's `None`.