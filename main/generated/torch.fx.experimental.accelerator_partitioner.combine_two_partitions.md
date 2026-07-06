# torch.fx.experimental.accelerator_partitioner.combine_two_partitions

torch.fx.experimental.accelerator_partitioner.combine_two_partitions(*partition_0*, *partition_1*, *partitions*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/fx/experimental/accelerator_partitioner.py#L80)

Given a list of partitions and its two partitions,
combine these two partitions into a new one appending to the partitions
and remove the previous two partitions from the list of partitions