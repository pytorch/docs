# torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule

torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule(*n*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/fx/experimental/graph_gradual_typechecker.py#L287)

Without dynamism, the rule checks that the
product of the elements of the argument tensor
type is equal to the product of the elements
of the required shape. We gradualize this rule
by adding a case to handle fully dynamic input
as well as input where some of the tensor dimensions
are unknown. In this case we check for divisibility

Return type:

*TensorType*