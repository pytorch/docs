# torch.fx.experimental.accelerator_partitioner.check_dependency

torch.fx.experimental.accelerator_partitioner.check_dependency(*partition*)[[source]](https://github.com/pytorch/pytorch/blob/c8532b3e7f0e3aec4bb518524c3ca041e17665aa/torch/fx/experimental/accelerator_partitioner.py#L271)

Given a partition,check if there is a circular dependency on
this partition using bfs

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)