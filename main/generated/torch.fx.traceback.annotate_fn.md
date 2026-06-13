# torch.fx.traceback.annotate_fn

torch.fx.traceback.annotate_fn(*annotation_dict*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/fx/traceback.py#L386)

A decorator that wraps a function with the annotate context manager.
Use this when you want to annotate an entire function instead of a specific code block.

Note

This API is **not backward compatible** and may evolve in future releases.

Note

This API is not compatible with fx.symbolic_trace or jit.trace. It's intended
to be used with PT2 family of tracers, e.g. torch.export and dynamo.

Parameters:

**annotation_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - A dictionary of custom key-value pairs to inject
into the FX trace metadata for all operations in the function.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]]

Example

All operations in my_function will have {"pp_stage": 1} in their metadata.

```
>>> @annotate_fn({"pp_stage": 1})
... def my_function(x):
... return x + 1
```

Warning

This API is experimental and is *NOT* backward-compatible.