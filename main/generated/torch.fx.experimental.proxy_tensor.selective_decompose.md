# torch.fx.experimental.proxy_tensor.selective_decompose

torch.fx.experimental.proxy_tensor.selective_decompose(*joint_gm*, **args*, *decomposition*, *should_decompose*, *trace_joint_graph*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/proxy_tensor.py#L2423)

Retrace a joint graph module and selectively apply decomposition.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)