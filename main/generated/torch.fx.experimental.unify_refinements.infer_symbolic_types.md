# torch.fx.experimental.unify_refinements.infer_symbolic_types

torch.fx.experimental.unify_refinements.infer_symbolic_types(*traced*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/fx/experimental/unify_refinements.py#L32)

Calls our symbolic inferencer twice.
This is useful when one pass is not enough
to infer all the information such as the case
for broadcasting.