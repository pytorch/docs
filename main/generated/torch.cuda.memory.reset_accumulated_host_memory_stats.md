# torch.cuda.memory.reset_accumulated_host_memory_stats

torch.cuda.memory.reset_accumulated_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/cuda/memory.py#L458)

Reset the "accumulated" (historical) stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict.