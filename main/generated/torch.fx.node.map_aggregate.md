# torch.fx.node.map_aggregate

torch.fx.node.map_aggregate(*a*, *fn*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/node.py#L929)

Apply fn recursively to each object appearing in arg.

arg may be a list, tuple, slice, or dict with string keys: the return value will
have the same type and structure.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

*ArgumentT*