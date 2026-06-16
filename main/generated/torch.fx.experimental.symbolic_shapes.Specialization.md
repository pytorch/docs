# Specialization

*class*torch.fx.experimental.symbolic_shapes.Specialization(*source*, *check_fn*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/fx/experimental/symbolic_shapes.py#L1164)

This class is used in multi-graph compilation contexts where we generate
multiple specialized graphs and dispatch to the appropriate one at runtime.
This allows us to optimize the trade-off between performance and generality
by creating specialized versions for common patterns (e.g., x.shape[0] % 16 == 0)
while maintaining a general fallback.