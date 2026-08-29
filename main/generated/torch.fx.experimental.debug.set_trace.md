# torch.fx.experimental.debug.set_trace

torch.fx.experimental.debug.set_trace(*gm*)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/fx/experimental/debug.py#L9)

Sets a breakpoint in gm's generated python code. It drops into pdb when
gm gets run.

Parameters:

**gm** ([*GraphModule*](../fx.html#torch.fx.GraphModule)) - graph module to insert breakpoint. It is then recompiled for it to
take effect.

Returns:

the gm with breakpoint inserted.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)