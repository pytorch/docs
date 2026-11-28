# torch.fx.experimental.proxy_tensor.selective_decompose

torch.fx.experimental.proxy_tensor.selective_decompose(*joint_gm*, **args*, *decomposition*, *should_decompose*, *trace_joint_graph*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/experimental/proxy_tensor.py#L2563)

Retrace a joint graph module and selectively apply decomposition.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)