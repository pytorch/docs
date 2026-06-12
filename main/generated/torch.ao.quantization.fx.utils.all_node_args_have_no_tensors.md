# all_node_args_have_no_tensors

*class*torch.ao.quantization.fx.utils.all_node_args_have_no_tensors(*node*, *modules*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/ao/quantization/fx/utils.py#L285)

If we know for sure that all of this node's args have no
tensors (are primitives), return True. If we either
find a tensor or are not sure, return False. Note: this
function is not exact.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)