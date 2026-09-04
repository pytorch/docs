# torch.fx.experimental.optimization.use_mkl_length

torch.fx.experimental.optimization.use_mkl_length(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/optimization.py#L294)

This is a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by checking if there
are more than 2 nodes in it

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)