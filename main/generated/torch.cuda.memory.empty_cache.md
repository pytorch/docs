# torch.cuda.memory.empty_cache

torch.cuda.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/cuda/memory.py#L222)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other GPU application and visible in
nvidia-smi.

Note

`empty_cache()` doesn't increase the amount of GPU
memory available for PyTorch. However, it may help reduce fragmentation
of GPU memory in certain cases. See [Memory management](../notes/cuda.html#cuda-memory-management) for
more details about GPU memory management.