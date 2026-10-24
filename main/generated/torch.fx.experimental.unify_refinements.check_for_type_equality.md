# torch.fx.experimental.unify_refinements.check_for_type_equality

torch.fx.experimental.unify_refinements.check_for_type_equality(*g1*, *g2*)[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/fx/experimental/unify_refinements.py#L130)

A check equality to be used in fixed points.
We do not use graph equality but instead type
equality.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)