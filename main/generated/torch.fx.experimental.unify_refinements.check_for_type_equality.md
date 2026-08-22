# torch.fx.experimental.unify_refinements.check_for_type_equality

torch.fx.experimental.unify_refinements.check_for_type_equality(*g1*, *g2*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/fx/experimental/unify_refinements.py#L130)

A check equality to be used in fixed points.
We do not use graph equality but instead type
equality.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)