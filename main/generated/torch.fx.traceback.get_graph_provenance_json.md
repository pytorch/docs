# torch.fx.traceback.get_graph_provenance_json

torch.fx.traceback.get_graph_provenance_json(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/fx/traceback.py#L532)

Given an fx.Graph, return a json that contains the provenance information of each node.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]