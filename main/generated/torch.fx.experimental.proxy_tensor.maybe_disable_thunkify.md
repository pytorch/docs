# torch.fx.experimental.proxy_tensor.maybe_disable_thunkify

torch.fx.experimental.proxy_tensor.maybe_disable_thunkify()[[source]](https://github.com/pytorch/pytorch/blob/2a8ba15825312e681c7dc6b12b79dec216aecd30/torch/fx/experimental/proxy_tensor.py#L783)

Within a context, disable thunkification. See [`maybe_enable_thunkify()`](torch.fx.experimental.proxy_tensor.maybe_enable_thunkify.html#torch.fx.experimental.proxy_tensor.maybe_enable_thunkify)
for more details. This is helpful if you have a wrapper function which
you want to enable thunkification on, but in some segment on the inside (say,
the original user function), you want to disable thunkification as you know
it is not needed there.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]