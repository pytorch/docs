# torch.xpu.memory.change_current_allocator

torch.xpu.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/xpu/memory.py#L529)

Change the currently used memory allocator to be the one provided.

Note

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.xpu.memory._XPUAllocator*) - allocator to be set as the active one.