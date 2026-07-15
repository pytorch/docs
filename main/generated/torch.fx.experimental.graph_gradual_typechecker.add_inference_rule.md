# torch.fx.experimental.graph_gradual_typechecker.add_inference_rule

torch.fx.experimental.graph_gradual_typechecker.add_inference_rule(*n*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/fx/experimental/graph_gradual_typechecker.py#L164)

Apply the addition inference rule. This includes:
- scalar addition
- broadcasting semantics

Note that we always return the least precise type between
the operands (after applying broadcasting) to be the final type of the operation

Note that we do not modify the operand types themselves after applying broadcasting
to them. We only use them to calculate the final type

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)