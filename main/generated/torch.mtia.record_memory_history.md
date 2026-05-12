# torch.mtia.record_memory_history

torch.mtia.record_memory_history(*enabled='all'*, *stacks='python'*, *max_entries=0*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/mtia/__init__.py#L205)

Enable/Disable the memory profiler on MTIA allocator

Parameters:

- **enabled** (*all**or**state**,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).
- **stacks** (*"python"**or**"cpp"**,**optional*) -
- **max_entries** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) -