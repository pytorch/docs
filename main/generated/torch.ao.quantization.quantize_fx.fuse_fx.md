# fuse_fx

*class*torch.ao.quantization.quantize_fx.fuse_fx(*model*, *fuse_custom_config=None*, *backend_config=None*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/ao/quantization/quantize_fx.py#L204)

Fuse modules like conv+bn, conv+bn+relu etc, model must be in eval mode.
Fusion rules are defined in torch.ao.quantization.fx.fusion_pattern.py

Parameters:

- **model** (***) - a torch.nn.Module model
- **fuse_custom_config** (***) - custom configurations for fuse_fx.
See [`FuseCustomConfig`](torch.ao.quantization.fx.custom_config.FuseCustomConfig.html#torch.ao.quantization.fx.custom_config.FuseCustomConfig) for more details

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)

Example:

```
from torch.ao.quantization import fuse_fx

m = Model().eval()
m = fuse_fx(m)
```