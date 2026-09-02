# torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected

torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected(*subgraph1*, *subgraph2*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/passes/utils/source_matcher_utils.py#L177)

Given two subgraphs A and B (in the form of a list of nodes), checks if
A has nodes connecting to at least one node in B - aka there exists a node
in B that uses a node in A (not the other way around).

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)