# torch.cuda.memory.reset_peak_host_memory_stats

torch.cuda.memory.reset_peak_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/memory.py#L471)

Reset the "peak" stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.