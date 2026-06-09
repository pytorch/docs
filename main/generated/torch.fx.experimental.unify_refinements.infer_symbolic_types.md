# torch.fx.experimental.unify_refinements.infer_symbolic_types

torch.fx.experimental.unify_refinements.infer_symbolic_types(*traced*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/unify_refinements.py#L32)

Calls our symbolic inferencer twice.
This is useful when one pass is not enough
to infer all the information such as the case
for broadcasting.