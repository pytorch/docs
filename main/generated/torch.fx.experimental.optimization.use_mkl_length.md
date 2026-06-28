# torch.fx.experimental.optimization.use_mkl_length

torch.fx.experimental.optimization.use_mkl_length(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/experimental/optimization.py#L292)

This is a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by checking if there
are more than 2 nodes in it

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)