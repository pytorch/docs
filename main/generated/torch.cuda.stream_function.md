# torch.cuda.stream

torch.cuda.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/cuda/__init__.py#L966)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This manager is a no-op if it's
`None`.

Return type:

[*StreamContext*](torch.cuda.StreamContext.html#torch.cuda.StreamContext)

Note

In eager mode stream is of type Stream class while in JIT it is
an object of the custom class `torch.classes.cuda.Stream`.