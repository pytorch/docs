# torch.mps.stream

torch.mps.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/mps/streams.py#L58)

Context manager that selects a given stream.

MPS operators called within this context will be enqueued on the selected
stream.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This manager is a no-op if it's `None`.