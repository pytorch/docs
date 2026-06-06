# torch.fx.experimental.accelerator_partitioner.check_dependency

torch.fx.experimental.accelerator_partitioner.check_dependency(*partition*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/fx/experimental/accelerator_partitioner.py#L271)

Given a partition,check if there is a circular dependency on
this partition using bfs

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)