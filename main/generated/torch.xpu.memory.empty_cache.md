# torch.xpu.memory.empty_cache

torch.xpu.memory.empty_cache()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/memory.py#L26)

Release all unoccupied cached memory currently held by the caching
allocator so that those can be used in other XPU application.

Note

`empty_cache()` doesn't increase the amount of XPU
memory available for PyTorch. However, it may help reduce fragmentation
of XPU memory in certain cases.