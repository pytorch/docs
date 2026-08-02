# graph_module_from_producer_nodes

*class*torch.ao.quantization.fx.utils.graph_module_from_producer_nodes(*root*, *producer_nodes*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/ao/quantization/fx/utils.py#L221)

Construct a graph module from extracted producer nodes
from collect_producer_nodes function
:param root: the root module for the original graph
:param producer_nodes: a list of nodes we use to construct the graph

Returns:

A graph module constructed from the producer nodes

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)