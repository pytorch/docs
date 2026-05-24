# torch.fx.passes.operator_support.create_op_support

torch.fx.passes.operator_support.create_op_support(*is_node_supported*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/fx/passes/operator_support.py#L141)

Wraps a IsNodeSupported function into an OperatorSupportBase instance

> IsNodeSupported has the same call signature as
> OperatorSupportBase.is_node_supported

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*