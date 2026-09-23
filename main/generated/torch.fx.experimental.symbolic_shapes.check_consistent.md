# torch.fx.experimental.symbolic_shapes.check_consistent

torch.fx.experimental.symbolic_shapes.check_consistent(*new*, *old*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/fx/experimental/symbolic_shapes.py#L553)

Test that two "meta" values (typically either Tensor or SymInt) have
the same values, e.g., after retracing. If we don't understand the
quantities in question, we'll just skip the consistency check.