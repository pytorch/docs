# torch.fx.passes.operator_support.chain

torch.fx.passes.operator_support.chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/passes/operator_support.py#L158)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns False if
any of it reports False.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*