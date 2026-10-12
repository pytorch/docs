# torch.fx.experimental.accelerator_partitioner.check_dependency

torch.fx.experimental.accelerator_partitioner.check_dependency(*partition*)[[source]](https://github.com/pytorch/pytorch/blob/44a629b353df33cd84f67a031bba5b6313160a1c/torch/fx/experimental/accelerator_partitioner.py#L271)

Given a partition,check if there is a circular dependency on
this partition using bfs

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)