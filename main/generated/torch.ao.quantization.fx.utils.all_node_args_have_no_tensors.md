# all_node_args_have_no_tensors

*class*torch.ao.quantization.fx.utils.all_node_args_have_no_tensors(*node*, *modules*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/ao/quantization/fx/utils.py#L285)

If we know for sure that all of this node's args have no
tensors (are primitives), return True. If we either
find a tensor or are not sure, return False. Note: this
function is not exact.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)