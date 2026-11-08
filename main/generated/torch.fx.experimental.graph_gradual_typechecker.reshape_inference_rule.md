# torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule

torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule(*n*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/graph_gradual_typechecker.py#L287)

Without dynamism, the rule checks that the
product of the elements of the argument tensor
type is equal to the product of the elements
of the required shape. We gradualize this rule
by adding a case to handle fully dynamic input
as well as input where some of the tensor dimensions
are unknown. In this case we check for divisibility

Return type:

*TensorType*