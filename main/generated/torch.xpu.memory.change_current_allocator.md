# torch.xpu.memory.change_current_allocator

torch.xpu.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/xpu/memory.py#L529)

Change the currently used memory allocator to be the one provided.

Note

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.xpu.memory._XPUAllocator*) - allocator to be set as the active one.