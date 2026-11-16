# torch.mps.stream

torch.mps.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/mps/streams.py#L58)

Context manager that selects a given stream.

MPS operators called within this context will be enqueued on the selected
stream.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This manager is a no-op if it's `None`.