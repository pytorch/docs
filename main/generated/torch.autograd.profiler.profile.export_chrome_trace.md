# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*, *metadata=None*, *use_python_export=False*, *cuda_graph_annotations=None*, *graph_lanes='none'*, *default_stream=7*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/autograd/profiler.py#L542)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Path where the trace will be written.