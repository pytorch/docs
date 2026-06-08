# torch.fx.experimental.proxy_tensor.make_fx

torch.fx.experimental.proxy_tensor.make_fx(*f*, *decomposition_table=None*, *tracing_mode='real'*, *_allow_non_fake_inputs=False*, ***, *pre_dispatch=False*, *record_module_stack=False*, *_allow_fake_constant=False*, *_error_on_data_dependent_ops=True*, *record_stack_traces=False*, *proxy_module_inputs=False*, *_disable_torch_fn_metadata_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/fx/experimental/proxy_tensor.py#L3015)

Given a function f, return a new function which when executed with valid
arguments to f, returns an FX GraphModule representing the set of operations that
were executed during the course of execution.

If record_stack_traces is True, the stack trace will be preserved on node.meta["stack_trace"]

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*GraphModule*](../fx.html#torch.fx.GraphModule)]