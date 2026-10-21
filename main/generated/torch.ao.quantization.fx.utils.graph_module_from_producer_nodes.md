# graph_module_from_producer_nodes

*class*torch.ao.quantization.fx.utils.graph_module_from_producer_nodes(*root*, *producer_nodes*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/ao/quantization/fx/utils.py#L221)

Construct a graph module from extracted producer nodes
from collect_producer_nodes function
:param root: the root module for the original graph
:param producer_nodes: a list of nodes we use to construct the graph

Returns:

A graph module constructed from the producer nodes

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)