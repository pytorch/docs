# all_node_args_have_no_tensors

*class*torch.ao.quantization.fx.utils.all_node_args_have_no_tensors(*node*, *modules*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/ao/quantization/fx/utils.py#L285)

If we know for sure that all of this node's args have no
tensors (are primitives), return True. If we either
find a tensor or are not sure, return False. Note: this
function is not exact.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)