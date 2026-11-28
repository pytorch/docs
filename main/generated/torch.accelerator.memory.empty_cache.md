# torch.accelerator.memory.empty_cache

torch.accelerator.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/accelerator/memory.py#L24)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other applications.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.