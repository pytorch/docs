# torch.fx.experimental.proxy_tensor.make_fx

torch.fx.experimental.proxy_tensor.make_fx(*f*, *decomposition_table=None*, *tracing_mode='real'*, *_allow_non_fake_inputs=False*, ***, *pre_dispatch=False*, *record_module_stack=False*, *_allow_fake_constant=False*, *_error_on_data_dependent_ops=True*, *record_stack_traces=False*, *proxy_module_inputs=False*, *_disable_torch_fn_metadata_mode=False*, *dynamic_shapes=None*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/proxy_tensor.py#L3281)

Given a function f, return a new function which when executed with valid
arguments to f, returns an FX GraphModule representing the set of operations that
were executed during the course of execution.

If record_stack_traces is True, the stack trace will be preserved on node.meta["stack_trace"]

`tracing_mode`:

- `"real"`: no fakification, traces with real tensors.
- `"fake"`: tensors become FakeTensors. By default all dims are
static (concrete); if `dynamic_shapes` is set, the spec
controls which dims become unbacked symbolic sizes -- everything
not declared by the spec stays static.
- `"symbolic"`: tensors become FakeTensors and **every dim becomes a
backed symbolic size**. NOTE: using backed symbols this way is generally
**not recommended and not sound** -- backed symbols come with assumptions
and can be constrained by guards silently. Kept for backward compatibility.
Prefer `"fake"` + `dynamic_shapes` to declare dynamism explicitly with
unbacked symbols.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*GraphModule*](../fx.html#torch.fx.GraphModule)]