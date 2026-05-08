# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/autograd/profiler.py#L519)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.