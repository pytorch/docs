# torch.mtia.record_memory_history

torch.mtia.record_memory_history(*enabled='all'*, *stacks='python'*, *max_entries=0*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/mtia/__init__.py#L205)

Enable/Disable the memory profiler on MTIA allocator

Parameters:

- **enabled** (*all**or**state**,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).
- **stacks** (*"python"**or**"cpp"**,**optional*) -
- **max_entries** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) -