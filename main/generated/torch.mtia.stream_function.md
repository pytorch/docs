# torch.mtia.stream

torch.mtia.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/mtia/__init__.py#L387)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.mtia.Stream_class.html#torch.mtia.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Return type:

[*StreamContext*](torch.mtia.StreamContext.html#torch.mtia.StreamContext)

Note

In eager mode stream is of type Stream class while in JIT it doesn't support torch.mtia.stream