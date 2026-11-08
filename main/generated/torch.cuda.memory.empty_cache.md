# torch.cuda.memory.empty_cache

torch.cuda.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/memory.py#L222)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other GPU application and visible in
nvidia-smi.

Note

`empty_cache()` doesn't increase the amount of GPU
memory available for PyTorch. However, it may help reduce fragmentation
of GPU memory in certain cases. See [Memory management](../notes/cuda.html#cuda-memory-management) for
more details about GPU memory management.