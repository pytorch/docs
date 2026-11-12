# torch.fx.experimental.accelerator_partitioner.check_dependency

torch.fx.experimental.accelerator_partitioner.check_dependency(*partition*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/fx/experimental/accelerator_partitioner.py#L271)

Given a partition,check if there is a circular dependency on
this partition using bfs

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)