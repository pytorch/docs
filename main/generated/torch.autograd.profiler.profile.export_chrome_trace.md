# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/autograd/profiler.py#L519)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.