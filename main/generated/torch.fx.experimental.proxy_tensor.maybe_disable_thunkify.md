# torch.fx.experimental.proxy_tensor.maybe_disable_thunkify

torch.fx.experimental.proxy_tensor.maybe_disable_thunkify()[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/fx/experimental/proxy_tensor.py#L792)

Within a context, disable thunkification. See [`maybe_enable_thunkify()`](torch.fx.experimental.proxy_tensor.maybe_enable_thunkify.html#torch.fx.experimental.proxy_tensor.maybe_enable_thunkify)
for more details. This is helpful if you have a wrapper function which
you want to enable thunkification on, but in some segment on the inside (say,
the original user function), you want to disable thunkification as you know
it is not needed there.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]