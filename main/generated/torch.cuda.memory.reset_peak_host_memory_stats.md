# torch.cuda.memory.reset_peak_host_memory_stats

torch.cuda.memory.reset_peak_host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/cuda/memory.py#L468)

Reset the "peak" stats tracked by the host memory allocator.

See `host_memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.