# Specialization

*class*torch.fx.experimental.symbolic_shapes.Specialization(*source*, *check_fn*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/fx/experimental/symbolic_shapes.py#L1158)

This class is used in multi-graph compilation contexts where we generate
multiple specialized graphs and dispatch to the appropriate one at runtime.
This allows us to optimize the trade-off between performance and generality
by creating specialized versions for common patterns (e.g., x.shape[0] % 16 == 0)
while maintaining a general fallback.