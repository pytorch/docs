# torch.fx.experimental.proxy_tensor.selective_decompose

torch.fx.experimental.proxy_tensor.selective_decompose(*joint_gm*, **args*, *decomposition*, *should_decompose*, *trace_joint_graph*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/proxy_tensor.py#L2250)

Retrace a joint graph module and selectively apply decomposition.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)