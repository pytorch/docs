# torch.fx.experimental.graph_gradual_typechecker.linear_check

torch.fx.experimental.graph_gradual_typechecker.linear_check(*tensor_type*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/graph_gradual_typechecker.py#L520)

Checks that an input tensor type satisfies the conditions for linear operation
and returns the output type based on in and out features given by module_instance

Return type:

*TensorType*