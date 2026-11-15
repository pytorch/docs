# torch.fx.passes.operator_support.create_op_support

torch.fx.passes.operator_support.create_op_support(*is_node_supported*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/fx/passes/operator_support.py#L141)

Wraps a IsNodeSupported function into an OperatorSupportBase instance

> IsNodeSupported has the same call signature as
> OperatorSupportBase.is_node_supported

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*