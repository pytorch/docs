# torch.fx.experimental.graph_gradual_typechecker.linear_check

torch.fx.experimental.graph_gradual_typechecker.linear_check(*tensor_type*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/fx/experimental/graph_gradual_typechecker.py#L520)

Checks that an input tensor type satisfies the conditions for linear operation
and returns the output type based on in and out features given by module_instance

Return type:

*TensorType*