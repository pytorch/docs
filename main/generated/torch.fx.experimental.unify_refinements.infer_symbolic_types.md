# torch.fx.experimental.unify_refinements.infer_symbolic_types

torch.fx.experimental.unify_refinements.infer_symbolic_types(*traced*)[[source]](https://github.com/pytorch/pytorch/blob/a84b7baa33f893ab92176c08a85b14455e60b2fc/torch/fx/experimental/unify_refinements.py#L32)

Calls our symbolic inferencer twice.
This is useful when one pass is not enough
to infer all the information such as the case
for broadcasting.