# torch.fx.experimental.proxy_tensor.maybe_disable_thunkify

torch.fx.experimental.proxy_tensor.maybe_disable_thunkify()[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/fx/experimental/proxy_tensor.py#L793)

Within a context, disable thunkification. See [`maybe_enable_thunkify()`](torch.fx.experimental.proxy_tensor.maybe_enable_thunkify.html#torch.fx.experimental.proxy_tensor.maybe_enable_thunkify)
for more details. This is helpful if you have a wrapper function which
you want to enable thunkification on, but in some segment on the inside (say,
the original user function), you want to disable thunkification as you know
it is not needed there.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]