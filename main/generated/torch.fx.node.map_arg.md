# torch.fx.node.map_arg

torch.fx.node.map_arg(*a*, *fn*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/node.py#L917)

Apply fn recursively to each Node appearing in arg.

arg may be a list, tuple, slice, or dict with string keys: the return value will
have the same type and structure.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

*ArgumentT*