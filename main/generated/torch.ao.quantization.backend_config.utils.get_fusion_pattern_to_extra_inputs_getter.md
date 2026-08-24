# get_fusion_pattern_to_extra_inputs_getter

*class*torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_extra_inputs_getter(*backend_config*)[[source]](https://github.com/pytorch/pytorch/blob/9bc1ff884cb38c4f6485d73c20a922b782335b34/torch/ao/quantization/backend_config/utils.py#L124)

Get a map from fusion pattern to a function that returns extra input nodes
from the fusion pattern, in the order required by the root node. This is optional,
if not specified, we will not copy over any extra inputs for the root node.

Example:

```
# Let's say we have the pattern (torch.add, MatchAllNode, (torch.nn.BatchNorm2d, torch.nn.Conv2d))
# and root node is torch.nn.Conv2d, and the node in MatchAllNode would be an extra
# argument to the fused module, we can unpack the pattern and return the node at
# MatchAllNode here
# we can implement extra_inputs_getter as follows:
def extra_inputs_getter(pattern) -> List[Any]:
 add, extra_input, conv_pattern = pattern
 return [extra_input]
```

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[Pattern](torch.ao.quantization.utils.Pattern.html#torch.ao.quantization.utils.Pattern), [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)]