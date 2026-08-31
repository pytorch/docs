# Specialization

*class*torch.fx.experimental.symbolic_shapes.Specialization(*source*, *check_fn*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/fx/experimental/symbolic_shapes.py#L1174)

This class is used in multi-graph compilation contexts where we generate
multiple specialized graphs and dispatch to the appropriate one at runtime.
This allows us to optimize the trade-off between performance and generality
by creating specialized versions for common patterns (e.g., x.shape[0] % 16 == 0)
while maintaining a general fallback.