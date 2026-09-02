# FlopCounterMode

*class*torch.utils.flop_counter.FlopCounterMode(*mods=None*, *depth=2*, *display=True*, *custom_mapping=None*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/utils/flop_counter.py#L887)

Count theoretical FLOPs for operators that run inside the context.

`FlopCounterMode` uses `TorchDispatchMode` to intercept operations and
apply registered FLOP formulas. Counts are shape-based and formula-defined;
unsupported operations contribute zero FLOPs unless they decompose into
supported operations.

The optional `mods` argument is no longer needed for module attribution.
When `display` is true, exiting the context prints a table. Use
`get_total_flops()` or `get_flop_counts()` to read the same information
programmatically.

Example usage:

```
mod = ...
inp = ...

with FlopCounterMode(display=False) as flop_counter:
 mod(inp).sum().backward()

total = flop_counter.get_total_flops()
```

get_flop_counts()[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/utils/flop_counter.py#L938)

Return the flop counts as a dictionary of dictionaries.

The outer
dictionary is keyed by module name, and the inner dictionary is keyed by
operation name.

Returns:

The flop counts as a dictionary.

Return type:

Dict[[str](https://docs.python.org/3/library/stdtypes.html#str), Dict[Any, [int](https://docs.python.org/3/library/functions.html#int)]]