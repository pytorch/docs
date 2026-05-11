# torch.accelerator.memory.empty_cache

torch.accelerator.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/accelerator/memory.py#L23)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other application.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.