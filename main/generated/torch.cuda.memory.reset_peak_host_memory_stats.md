# torch.cuda.memory.reset_peak_host_memory_stats

torch.cuda.memory.reset_peak_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/cuda/memory.py#L467)

Reset the "peak" stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.