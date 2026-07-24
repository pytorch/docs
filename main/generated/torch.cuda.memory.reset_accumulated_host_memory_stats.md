# torch.cuda.memory.reset_accumulated_host_memory_stats

torch.cuda.memory.reset_accumulated_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/memory.py#L462)

Reset the "accumulated" (historical) stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict.