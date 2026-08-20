# torch.xpu.memory.change_current_allocator

torch.xpu.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/xpu/memory.py#L532)

Change the currently used memory allocator to be the one provided.

Note

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.xpu.memory._XPUAllocator*) - allocator to be set as the active one.