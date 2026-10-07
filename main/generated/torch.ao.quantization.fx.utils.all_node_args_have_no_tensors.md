# all_node_args_have_no_tensors

*class*torch.ao.quantization.fx.utils.all_node_args_have_no_tensors(*node*, *modules*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/80b434f9a9e9f3dd439f5883f376326e470526ff/torch/ao/quantization/fx/utils.py#L285)

If we know for sure that all of this node's args have no
tensors (are primitives), return True. If we either
find a tensor or are not sure, return False. Note: this
function is not exact.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)