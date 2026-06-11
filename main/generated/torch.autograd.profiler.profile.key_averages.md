# torch.autograd.profiler.profile.key_averages

profile.key_averages(*group_by_input_shape=False*, *group_by_stack_n=0*, *group_by_overload_name=False*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/autograd/profiler.py#L568)

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

Returns:

An EventList containing FunctionEventAvg objects.