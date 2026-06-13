# torch.fx.experimental.proxy_tensor.maybe_enable_thunkify

torch.fx.experimental.proxy_tensor.maybe_enable_thunkify()[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/fx/experimental/proxy_tensor.py#L779)

Within this context manager, if you are doing make_fx tracing, we will thunkify
all SymNode compute and avoid tracing it into the graph unless it is actually needed.
You should prefer to avoid using this as much as possible, as lazy evaluation of
SymNode tracing can lead to long chains of thunks which will stack overflow
if you evaluate them. However, this is currently sometimes necessary as there
are buggy parts of PT2 which will fail with "s0 is not tracked with proxy" error
due to insufficient tracing of SymNode computation.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]