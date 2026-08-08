# torch.fx.experimental.optimization.use_mkl_length

torch.fx.experimental.optimization.use_mkl_length(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/fx/experimental/optimization.py#L294)

This is a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by checking if there
are more than 2 nodes in it

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)