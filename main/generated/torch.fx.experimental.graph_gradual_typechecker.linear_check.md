# torch.fx.experimental.graph_gradual_typechecker.linear_check

torch.fx.experimental.graph_gradual_typechecker.linear_check(*tensor_type*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/graph_gradual_typechecker.py#L520)

Checks that an input tensor type satisfies the conditions for linear operation
and returns the output type based on in and out features given by module_instance

Return type:

*TensorType*