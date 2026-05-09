# torch.fx.experimental.accelerator_partitioner.check_dependency

torch.fx.experimental.accelerator_partitioner.check_dependency(*partition*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/fx/experimental/accelerator_partitioner.py#L271)

Given a partition,check if there is a circular dependency on
this partition using bfs

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)