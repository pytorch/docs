# torch.fx.passes.operator_support.any_chain

torch.fx.passes.operator_support.any_chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/50d50e722913b05a0762c886507c9be7ae43d2f3/torch/fx/passes/operator_support.py#L171)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns True if
any of it reports True.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*