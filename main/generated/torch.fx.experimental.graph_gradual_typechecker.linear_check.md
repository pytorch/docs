# torch.fx.experimental.graph_gradual_typechecker.linear_check

torch.fx.experimental.graph_gradual_typechecker.linear_check(*tensor_type*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/fx/experimental/graph_gradual_typechecker.py#L520)

Checks that an input tensor type satisfies the conditions for linear operation
and returns the output type based on in and out features given by module_instance

Return type:

*TensorType*