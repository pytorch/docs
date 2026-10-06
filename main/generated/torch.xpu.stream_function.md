# torch.xpu.stream

torch.xpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/xpu/__init__.py#L605)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's `None`.

Return type:

[*StreamContext*](torch.xpu.StreamContext.html#torch.xpu.StreamContext)