# torch.fx.traceback.get_graph_provenance_json

torch.fx.traceback.get_graph_provenance_json(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/fx/traceback.py#L574)

Given an fx.Graph, return a json that contains the provenance information of each node.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]