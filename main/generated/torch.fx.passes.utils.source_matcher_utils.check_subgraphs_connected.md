# torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected

torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected(*subgraph1*, *subgraph2*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/fx/passes/utils/source_matcher_utils.py#L177)

Given two subgraphs A and B (in the form of a list of nodes), checks if
A has nodes connecting to at least one node in B - aka there exists a node
in B that uses a node in A (not the other way around).

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)