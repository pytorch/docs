# torch.fx.experimental.unify_refinements.infer_symbolic_types

torch.fx.experimental.unify_refinements.infer_symbolic_types(*traced*)[[source]](https://github.com/pytorch/pytorch/blob/e5fed85d1847df3bfad77cb48791e6b5d4957cee/torch/fx/experimental/unify_refinements.py#L32)

Calls our symbolic inferencer twice.
This is useful when one pass is not enough
to infer all the information such as the case
for broadcasting.