# torch.fx.experimental.optimization.use_mkl_length

torch.fx.experimental.optimization.use_mkl_length(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/optimization.py#L294)

This is a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by checking if there
are more than 2 nodes in it

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)