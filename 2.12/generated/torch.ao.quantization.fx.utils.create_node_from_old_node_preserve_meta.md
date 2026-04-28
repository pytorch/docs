# create_node_from_old_node_preserve_meta

*class*torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta(*quantized_graph*, *create_node_args*, *old_node*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/ao/quantization/fx/utils.py#L464)

Creates new_node and copies the necessary metadata to it from old_node.

Return type:

[*Node*](../fx.html#torch.fx.Node)