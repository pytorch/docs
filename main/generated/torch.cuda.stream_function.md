# torch.cuda.stream

torch.cuda.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L966)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Return type:

[*StreamContext*](torch.cuda.StreamContext.html#torch.cuda.StreamContext)

Note

In eager mode stream is of type Stream class while in JIT it is
an object of the custom class `torch.classes.cuda.Stream`.