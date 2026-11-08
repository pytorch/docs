# torch.fx.experimental.proxy_tensor.selective_decompose

torch.fx.experimental.proxy_tensor.selective_decompose(*joint_gm*, **args*, *decomposition*, *should_decompose*, *trace_joint_graph*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/proxy_tensor.py#L2550)

Retrace a joint graph module and selectively apply decomposition.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)