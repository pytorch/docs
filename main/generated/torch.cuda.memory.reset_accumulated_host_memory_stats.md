# torch.cuda.memory.reset_accumulated_host_memory_stats

torch.cuda.memory.reset_accumulated_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/cuda/memory.py#L454)

Reset the "accumulated" (historical) stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict.