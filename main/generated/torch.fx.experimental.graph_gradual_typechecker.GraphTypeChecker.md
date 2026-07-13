# GraphTypeChecker

*class*torch.fx.experimental.graph_gradual_typechecker.GraphTypeChecker(*env*, *traced*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/fx/experimental/graph_gradual_typechecker.py#L649)

type_check()[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/fx/experimental/graph_gradual_typechecker.py#L654)

A gradual type checker for graphs
Effect: every node's field type will be
populated with a type after type-checking is done

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

type_check_node(*n*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/fx/experimental/graph_gradual_typechecker.py#L668)

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