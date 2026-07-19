# torch.fx.experimental.proxy_tensor.selective_decompose

torch.fx.experimental.proxy_tensor.selective_decompose(*joint_gm*, **args*, *decomposition*, *should_decompose*, *trace_joint_graph*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/fx/experimental/proxy_tensor.py#L2432)

Retrace a joint graph module and selectively apply decomposition.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)