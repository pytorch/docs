# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*, *metadata=None*, *use_python_export=False*, *cuda_graph_annotations=None*, *graph_lanes='none'*, *default_stream=7*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/autograd/profiler.py#L551)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.