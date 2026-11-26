# torch.fx.passes.operator_support.any_chain

torch.fx.passes.operator_support.any_chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/fx/passes/operator_support.py#L171)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns True if
any of it reports True.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*