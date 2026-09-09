# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*, *metadata=None*, *use_python_export=False*, *cuda_graph_annotations=None*, *graph_lanes='none'*, *default_stream=7*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/autograd/profiler.py#L548)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Path where the trace will be written.