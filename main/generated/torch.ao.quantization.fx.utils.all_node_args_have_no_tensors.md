# all_node_args_have_no_tensors

*class*torch.ao.quantization.fx.utils.all_node_args_have_no_tensors(*node*, *modules*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/ao/quantization/fx/utils.py#L285)

If we know for sure that all of this node's args have no
tensors (are primitives), return True. If we either
find a tensor or are not sure, return False. Note: this
function is not exact.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)