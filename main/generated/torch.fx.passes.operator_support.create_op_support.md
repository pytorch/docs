# torch.fx.passes.operator_support.create_op_support

torch.fx.passes.operator_support.create_op_support(*is_node_supported*)[[source]](https://github.com/pytorch/pytorch/blob/f6c4d435cf6682e89d565983c0975951782dc5e2/torch/fx/passes/operator_support.py#L141)

Wraps a IsNodeSupported function into an OperatorSupportBase instance

> IsNodeSupported has the same call signature as
> OperatorSupportBase.is_node_supported

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*