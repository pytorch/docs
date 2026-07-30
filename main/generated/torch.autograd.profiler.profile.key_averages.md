# torch.autograd.profiler.profile.key_averages

profile.key_averages(*group_by_input_shape=False*, *group_by_stack_n=0*, *group_by_overload_name=False*, *include_python_functions=False*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/autograd/profiler.py#L578)

Averages all function events over their keys.

Parameters:

- **group_by_input_shapes** - group entries by
(event name, input shapes) rather than just event name.
This is useful to see which input shapes contribute to the runtime
the most and may help with size-specific optimizations or
choosing the best candidates for quantization (aka fitting a roof line)
- **group_by_stack_n** - group by top n stack trace entries
- **group_by_overload_name** - Differentiate operators by their overload name e.g. aten::add.Tensor
- **separately** (*and aten::add.out will be aggregated*) -
- **include_python_functions** - include Python function events (e.g. individual
Python callsite entries captured with `with_stack=True`) in the
averages. By default these are excluded because they tend to appear as
misleading hotspots (e.g. `threading.py: wait`) that obscure the
real operator-level breakdown. Set to `True` to restore the raw
per-callsite view.

Returns:

An EventList containing FunctionEventAvg objects.