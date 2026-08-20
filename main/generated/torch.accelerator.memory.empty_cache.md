# torch.accelerator.memory.empty_cache

torch.accelerator.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/accelerator/memory.py#L23)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other applications.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.