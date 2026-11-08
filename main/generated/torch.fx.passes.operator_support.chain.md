# torch.fx.passes.operator_support.chain

torch.fx.passes.operator_support.chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/passes/operator_support.py#L158)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns False if
any of it reports False.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*