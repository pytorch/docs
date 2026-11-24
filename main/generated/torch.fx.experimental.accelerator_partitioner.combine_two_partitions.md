# torch.fx.experimental.accelerator_partitioner.combine_two_partitions

torch.fx.experimental.accelerator_partitioner.combine_two_partitions(*partition_0*, *partition_1*, *partitions*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/experimental/accelerator_partitioner.py#L80)

Given a list of partitions and its two partitions,
combine these two partitions into a new one appending to the partitions
and remove the previous two partitions from the list of partitions