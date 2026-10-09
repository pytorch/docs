# torch.xpu.memory.empty_cache

torch.xpu.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/xpu/memory.py#L26)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other XPU application.

Note

`empty_cache()` doesn't increase the amount of XPU
memory available for PyTorch. However, it may help reduce fragmentation
of XPU memory in certain cases.