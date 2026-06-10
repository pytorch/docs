# torch.fx.passes.operator_support.chain

torch.fx.passes.operator_support.chain(**op_support*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/passes/operator_support.py#L158)

Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase

instance by evaluating each input OperatorSupportBase instance, and returns False if
any of it reports False.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

*OperatorSupportBase*