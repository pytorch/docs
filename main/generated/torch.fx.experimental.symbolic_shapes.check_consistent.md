# torch.fx.experimental.symbolic_shapes.check_consistent

torch.fx.experimental.symbolic_shapes.check_consistent(*new*, *old*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/fx/experimental/symbolic_shapes.py#L551)

Test that two "meta" values (typically either Tensor or SymInt) have
the same values, e.g., after retracing. If we don't understand the
quantities in question, we'll just skip the consistency check.