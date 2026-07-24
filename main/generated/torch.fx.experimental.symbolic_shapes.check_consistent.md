# torch.fx.experimental.symbolic_shapes.check_consistent

torch.fx.experimental.symbolic_shapes.check_consistent(*new*, *old*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/symbolic_shapes.py#L552)

Test that two "meta" values (typically either Tensor or SymInt) have
the same values, e.g., after retracing. If we don't understand the
quantities in question, we'll just skip the consistency check.