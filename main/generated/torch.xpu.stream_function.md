# torch.xpu.stream

torch.xpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/xpu/__init__.py#L608)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's `None`.

Return type:

[*StreamContext*](torch.xpu.StreamContext.html#torch.xpu.StreamContext)