# torch.fx.experimental.symbolic_shapes.check_consistent

torch.fx.experimental.symbolic_shapes.check_consistent(*new*, *old*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/fx/experimental/symbolic_shapes.py#L553)

Test that two "meta" values (typically either Tensor or SymInt) have
the same values, e.g., after retracing. If we don't understand the
quantities in question, we'll just skip the consistency check.