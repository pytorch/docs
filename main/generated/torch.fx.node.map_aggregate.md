# torch.fx.node.map_aggregate

torch.fx.node.map_aggregate(*a*, *fn*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/node.py#L929)

Apply fn recursively to each object appearing in arg.

arg may be a list, tuple, slice, or dict with string keys: the return value will
have the same type and structure.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

*ArgumentT*