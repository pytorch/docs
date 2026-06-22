# create_node_from_old_node_preserve_meta

*class*torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta(*quantized_graph*, *create_node_args*, *old_node*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/ao/quantization/fx/utils.py#L460)

Creates new_node and copies the necessary metadata to it from old_node.

Return type:

[*Node*](../fx.html#torch.fx.Node)