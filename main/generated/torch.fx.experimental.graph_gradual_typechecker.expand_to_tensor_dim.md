# torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim

torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim(*t*, *n*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/fx/experimental/graph_gradual_typechecker.py#L63)

Expand a type to the desired tensor dimension if possible
Raise an error otherwise.
- t is the given type
- n is a number of dimensions to expand to

Return type:

*TensorType*