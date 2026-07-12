# torch.fx.experimental.unify_refinements.check_for_type_equality

torch.fx.experimental.unify_refinements.check_for_type_equality(*g1*, *g2*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/unify_refinements.py#L130)

A check equality to be used in fixed points.
We do not use graph equality but instead type
equality.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)