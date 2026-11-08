# torch.xpu.memory.change_current_allocator

torch.xpu.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/memory.py#L532)

Change the currently used memory allocator to be the one provided.

Note

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.xpu.memory._XPUAllocator*) - allocator to be set as the active one.