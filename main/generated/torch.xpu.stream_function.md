# torch.xpu.stream

torch.xpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/xpu/__init__.py#L607)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's `None`.

Return type:

[*StreamContext*](torch.xpu.StreamContext.html#torch.xpu.StreamContext)