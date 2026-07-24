# torch.accelerator.memory.empty_host_cache

torch.accelerator.memory.empty_host_cache()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/accelerator/memory.py#L35)

Release all unoccupied cached host (pinned) memory currently held by the host caching
allocator so that it can be used by other applications.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.