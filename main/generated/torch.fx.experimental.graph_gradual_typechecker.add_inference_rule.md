# torch.fx.experimental.graph_gradual_typechecker.add_inference_rule

torch.fx.experimental.graph_gradual_typechecker.add_inference_rule(*n*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/fx/experimental/graph_gradual_typechecker.py#L164)

Apply the addition inference rule. This includes:
- scalar addition
- broadcasting semantics

Note that we always return the least precise type between
the operands (after applying broadcasting) to be the final type of the operation

Note that we do not modify the operand types themselves after applying broadcasting
to them. We only use them to calculate the final type

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)