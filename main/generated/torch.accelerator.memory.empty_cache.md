# torch.accelerator.memory.empty_cache

torch.accelerator.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/accelerator/memory.py#L23)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other application.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.