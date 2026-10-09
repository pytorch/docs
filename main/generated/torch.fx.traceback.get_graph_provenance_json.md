# torch.fx.traceback.get_graph_provenance_json

torch.fx.traceback.get_graph_provenance_json(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/traceback.py#L601)

Given an fx.Graph, return a json that contains the provenance information of each node.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]