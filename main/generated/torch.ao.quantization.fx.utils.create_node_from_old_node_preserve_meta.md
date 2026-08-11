# create_node_from_old_node_preserve_meta

*class*torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta(*quantized_graph*, *create_node_args*, *old_node*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/quantization/fx/utils.py#L460)

Creates new_node and copies the necessary metadata to it from old_node.

Return type:

[*Node*](../fx.html#torch.fx.Node)