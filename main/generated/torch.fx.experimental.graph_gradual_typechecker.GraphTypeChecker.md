# GraphTypeChecker

*class*torch.fx.experimental.graph_gradual_typechecker.GraphTypeChecker(*env*, *traced*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/fx/experimental/graph_gradual_typechecker.py#L649)

type_check()[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/fx/experimental/graph_gradual_typechecker.py#L654)

A gradual type checker for graphs
Effect: every node's field type will be
populated with a type after type-checking is done

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

type_check_node(*n*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/fx/experimental/graph_gradual_typechecker.py#L668)

Type check a given fx node.
Current operations:
- Reshape
- Transpose
- Add
- Relu
- conv2d
- batchnorm2d
- flatten
- maxpool2d
- adaptiveavgpool2d
- linear

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)