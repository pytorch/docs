# torch.mtia.record_memory_history

torch.mtia.record_memory_history(*enabled='all'*, *stacks='python'*, *max_entries=0*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/mtia/__init__.py#L205)

Enable/Disable the memory profiler on MTIA allocator

Parameters:

- **enabled** (*all**or**state**,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).
- **stacks** (*"python"**or**"cpp"**,**optional*) -
- **max_entries** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) -