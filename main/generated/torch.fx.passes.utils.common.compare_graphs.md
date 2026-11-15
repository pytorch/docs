# torch.fx.passes.utils.common.compare_graphs

torch.fx.passes.utils.common.compare_graphs(*left*, *right*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/fx/passes/utils/common.py#L83)

Return True if two graphs are identical, i.e they

- have the same number of outputs in the same order
- have the same number of inputs in the same order
- have the same set of nodes, and identical connectivity

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)