# torch.fx.node.map_aggregate

torch.fx.node.map_aggregate(*a*, *fn*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/node.py#L928)

Apply fn recursively to each object appearing in arg.

arg may be a list, tuple, slice, or dict with string keys: the return value will
have the same type and structure.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

*ArgumentT*