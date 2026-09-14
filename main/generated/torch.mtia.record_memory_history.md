# torch.mtia.record_memory_history

torch.mtia.record_memory_history(*enabled='all'*, *stacks='python'*, *max_entries=0*)[[source]](https://github.com/pytorch/pytorch/blob/b8bd7cf750ea02a2390d8a5440261e2c6ed5ddc7/torch/mtia/__init__.py#L205)

Enable/Disable the memory profiler on MTIA allocator

Parameters:

- **enabled** (*all**or**state**,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).
- **stacks** (*"python"**or**"cpp"**,**optional*) -
- **max_entries** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) -