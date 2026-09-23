# Specialization

*class*torch.fx.experimental.symbolic_shapes.Specialization(*source*, *check_fn*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/fx/experimental/symbolic_shapes.py#L1174)

This class is used in multi-graph compilation contexts where we generate
multiple specialized graphs and dispatch to the appropriate one at runtime.
This allows us to optimize the trade-off between performance and generality
by creating specialized versions for common patterns (e.g., x.shape[0] % 16 == 0)
while maintaining a general fallback.