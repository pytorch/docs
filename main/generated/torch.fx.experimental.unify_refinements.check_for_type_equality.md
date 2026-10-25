# torch.fx.experimental.unify_refinements.check_for_type_equality

torch.fx.experimental.unify_refinements.check_for_type_equality(*g1*, *g2*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/fx/experimental/unify_refinements.py#L130)

A check equality to be used in fixed points.
We do not use graph equality but instead type
equality.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)