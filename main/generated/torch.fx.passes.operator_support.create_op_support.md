# torch.fx.passes.operator_support.create_op_support

torch.fx.passes.operator_support.create_op_support(*is_node_supported*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/passes/operator_support.py#L141)

Wraps a IsNodeSupported function into an OperatorSupportBase instance

> IsNodeSupported has the same call signature as
> OperatorSupportBase.is_node_supported

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*