# torch.fx.experimental.optimization.use_mkl_length

torch.fx.experimental.optimization.use_mkl_length(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/optimization.py#L294)

This is a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by checking if there
are more than 2 nodes in it

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)