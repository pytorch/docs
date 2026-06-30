# torch.fx.passes.operator_support.create_op_support

torch.fx.passes.operator_support.create_op_support(*is_node_supported*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/fx/passes/operator_support.py#L141)

Wraps a IsNodeSupported function into an OperatorSupportBase instance

> IsNodeSupported has the same call signature as
> OperatorSupportBase.is_node_supported

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*