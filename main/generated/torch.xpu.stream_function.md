# torch.xpu.stream

torch.xpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/xpu/__init__.py#L608)

Wrap around the Context-manager StreamContext that selects a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This manager is a no-op if it's `None`.

Return type:

[*StreamContext*](torch.xpu.StreamContext.html#torch.xpu.StreamContext)