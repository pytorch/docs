# torch.autograd.profiler.profile.export_chrome_trace

profile.export_chrome_trace(*path*, *metadata=None*, *use_python_export=False*, *cuda_graph_annotations=None*, *graph_lanes='none'*, *default_stream=7*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/autograd/profiler.py#L542)

Export an EventList as a Chrome tracing tools file.

The checkpoint can be later loaded and inspected under `chrome://tracing` URL.

Parameters:

**path** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Path where the trace will be written.