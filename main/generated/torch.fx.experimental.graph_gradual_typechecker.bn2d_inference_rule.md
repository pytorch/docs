# torch.fx.experimental.graph_gradual_typechecker.bn2d_inference_rule

torch.fx.experimental.graph_gradual_typechecker.bn2d_inference_rule(*n*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/fx/experimental/graph_gradual_typechecker.py#L330)

Given a BatchNorm2D instance and a node check the following conditions:
- the input type can be expanded to a size 4 tensor: t = (x_1, x_2, x_3, x_4)
- the current node type can be expanded to a size 4 tensor: t' = (x_1', x_2', x_3', x_4')
- t is consistent with t'
- x_2 is consistent with the module's num_features
- x_2' is consistent with the module's num_features
output type: the more precise type of t and t'

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)