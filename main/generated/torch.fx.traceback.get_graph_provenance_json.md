# torch.fx.traceback.get_graph_provenance_json

torch.fx.traceback.get_graph_provenance_json(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/traceback.py#L617)

Given an fx.Graph, return a json that contains the provenance information of each node.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]