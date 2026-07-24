# torch.fx.experimental.accelerator_partitioner.combine_two_partitions

torch.fx.experimental.accelerator_partitioner.combine_two_partitions(*partition_0*, *partition_1*, *partitions*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/accelerator_partitioner.py#L80)

Given a list of partitions and its two partitions,
combine these two partitions into a new one appending to the partitions
and remove the previous two partitions from the list of partitions