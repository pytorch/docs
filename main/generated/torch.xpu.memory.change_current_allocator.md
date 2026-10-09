# torch.xpu.memory.change_current_allocator

torch.xpu.memory.change_current_allocator(*allocator*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/xpu/memory.py#L532)

Change the currently used memory allocator to be the one provided.

Note

If the current allocator has already been used/initialized, this function will error.

Parameters:

**allocator** (*torch.xpu.memory._XPUAllocator*) - allocator to be set as the active one.