# torch.fx.experimental.symbolic_shapes.check_consistent

torch.fx.experimental.symbolic_shapes.check_consistent(*new*, *old*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/fx/experimental/symbolic_shapes.py#L552)

Test that two "meta" values (typically either Tensor or SymInt) have
the same values, e.g., after retracing. If we don't understand the
quantities in question, we'll just skip the consistency check.