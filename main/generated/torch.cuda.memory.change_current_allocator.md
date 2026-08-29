# torch.cuda.memory.change_current_allocator

torch.cuda.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/cuda/memory.py#L1345)

Change the currently used memory allocator to be the one provided.

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.cuda.memory._CUDAAllocator*) - allocator to be set as the active one.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on creating and using a custom allocator