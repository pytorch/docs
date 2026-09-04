# torch.cuda.memory.change_current_allocator

torch.cuda.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/cuda/memory.py#L1364)

Change the currently used memory allocator to be the one provided.

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.cuda.memory._CUDAAllocator*) - allocator to be set as the active one.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on creating and using a custom allocator