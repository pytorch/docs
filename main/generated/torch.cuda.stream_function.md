# torch.cuda.stream

torch.cuda.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/__init__.py#L937)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Return type:

[*StreamContext*](torch.cuda.StreamContext.html#torch.cuda.StreamContext)

Note

In eager mode stream is of type Stream class while in JIT it is
an object of the custom class `torch.classes.cuda.Stream`.