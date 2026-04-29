# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/autograd/profiler.py#L519)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.