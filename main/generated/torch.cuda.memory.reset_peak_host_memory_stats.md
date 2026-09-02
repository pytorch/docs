# torch.cuda.memory.reset_peak_host_memory_stats

torch.cuda.memory.reset_peak_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/memory.py#L462)

Reset the "peak" stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.