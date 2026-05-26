# torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim

torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim(*t*, *n*)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/fx/experimental/graph_gradual_typechecker.py#L63)

Expand a type to the desired tensor dimension if possible
Raise an error otherwise.
- t is the given type
- n is a number of dimensions to expand to

Return type:

*TensorType*