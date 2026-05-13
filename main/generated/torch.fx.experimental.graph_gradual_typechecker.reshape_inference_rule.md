# torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule

torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule(*n*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/fx/experimental/graph_gradual_typechecker.py#L287)

Without dynamism, the rule checks that the
product of the elements of the argument tensor
type is equal to the product of the elements
of the required shape. We gradualize this rule
by adding a case to handle fully dynamic input
as well as input where some of the tensor dimensions
are unknown. In this case we check for divisibility

Return type:

*TensorType*