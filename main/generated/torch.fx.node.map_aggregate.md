# torch.fx.node.map_aggregate

torch.fx.node.map_aggregate(*a*, *fn*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/node.py#L930)

Apply fn recursively to each object appearing in arg.

arg may be a list, tuple, slice, or dict with string keys: the return value will
have the same type and structure.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

*ArgumentT*