# torch.fx.experimental.unify_refinements.infer_symbolic_types

torch.fx.experimental.unify_refinements.infer_symbolic_types(*traced*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/fx/experimental/unify_refinements.py#L32)

Calls our symbolic inferencer twice.
This is useful when one pass is not enough
to infer all the information such as the case
for broadcasting.