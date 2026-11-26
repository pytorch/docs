# torch.cuda.memory.reset_accumulated_host_memory_stats

torch.cuda.memory.reset_accumulated_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/cuda/memory.py#L473)

Reset the "accumulated" (historical) stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict.