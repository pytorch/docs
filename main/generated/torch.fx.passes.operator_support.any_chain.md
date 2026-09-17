# torch.fx.passes.operator_support.any_chain

torch.fx.passes.operator_support.any_chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/65c295bfa29161891e39b83fac63c4f5417ffdc2/torch/fx/passes/operator_support.py#L171)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns True if
any of it reports True.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*