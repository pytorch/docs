# torch.accelerator.memory.empty_host_cache

torch.accelerator.memory.empty_host_cache()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/accelerator/memory.py#L35)

Release all unoccupied cached host (pinned) memory currently held by the host caching
allocator so that it can be used by other applications.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.