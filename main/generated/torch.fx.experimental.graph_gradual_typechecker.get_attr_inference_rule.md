# torch.fx.experimental.graph_gradual_typechecker.get_attr_inference_rule

torch.fx.experimental.graph_gradual_typechecker.get_attr_inference_rule(*n*, *traced*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/graph_gradual_typechecker.py#L230)

The current getattr rule only handles the shape attribute
Can be extended to other attributes
The most representative type we have is "Dyn" but the system
can be extended with more types, such as a type to represent shapes

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)