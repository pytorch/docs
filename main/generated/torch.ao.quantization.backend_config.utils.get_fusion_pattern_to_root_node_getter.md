# get_fusion_pattern_to_root_node_getter

*class*torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_root_node_getter(*backend_config*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/quantization/backend_config/utils.py#L103)

Get a map from fusion pattern to a function that returns the root node
from the fusion pattern, e.g. the most common one is:

```
def get_root_node(node_pattern):
 while not isinstance(node_pattern[-1], Node):
 node_pattern = node_pattern[-1]
 return node_pattern[-1]
```

This can work for all patterns whose root node is the "last node" in the pattern,
e.g. `(torch.add, MatchAllNode, (torch.ReLU, torch.Conv2d))`.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[Pattern](torch.ao.quantization.utils.Pattern.html#torch.ao.quantization.utils.Pattern), [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)]