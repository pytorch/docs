# torch.cuda.memory.empty_cache

torch.cuda.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/cuda/memory.py#L218)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other GPU application and visible in
nvidia-smi.

Note

`empty_cache()` doesn't increase the amount of GPU
memory available for PyTorch. However, it may help reduce fragmentation
of GPU memory in certain cases. See [Memory management](../notes/cuda.html#cuda-memory-management) for
more details about GPU memory management.