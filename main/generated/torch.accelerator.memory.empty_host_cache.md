# torch.accelerator.memory.empty_host_cache

torch.accelerator.memory.empty_host_cache()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/accelerator/memory.py#L36)

Release all unoccupied cached host (pinned) memory currently held by the host caching
allocator so that it can be used by other applications.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.