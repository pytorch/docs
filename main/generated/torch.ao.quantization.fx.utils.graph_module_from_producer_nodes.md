# graph_module_from_producer_nodes

*class*torch.ao.quantization.fx.utils.graph_module_from_producer_nodes(*root*, *producer_nodes*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/ao/quantization/fx/utils.py#L221)

Construct a graph module from extracted producer nodes
from collect_producer_nodes function
:param root: the root module for the original graph
:param producer_nodes: a list of nodes we use to construct the graph

Returns:

A graph module constructed from the producer nodes

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)