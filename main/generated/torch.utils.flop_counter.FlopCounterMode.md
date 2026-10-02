# FlopCounterMode

*class*torch.utils.flop_counter.FlopCounterMode(*mods=None*, *depth=2*, *display=True*, *custom_mapping=None*, *skip_unsupported=False*)[[source]](https://github.com/pytorch/pytorch/blob/dcd7ed975a6b090ec2bcf2360c28c9a263be8fe5/torch/utils/flop_counter.py#L950)

Count theoretical FLOPs for operators that run inside the context.

`FlopCounterMode` uses `TorchDispatchMode` to intercept operations and
apply registered FLOP formulas. Counts are shape-based and formula-defined;
unsupported operations contribute zero FLOPs unless they decompose into
supported operations.

The optional `mods` argument is no longer needed for module attribution.
When `display` is true, exiting the context prints a table. Use
`get_total_flops()` or `get_flop_counts()` to read the same information
programmatically.

Parameters:

- **mods** ([*Module*](torch.nn.Module.html#torch.nn.Module)*|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Module*](torch.nn.Module.html#torch.nn.Module)*]**|**None*) - Ignored; accepted for backward compatibility. Passing it emits a warning.
- **depth** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Maximum depth for hierarchical display (default: 2).
- **display** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether to print the FLOP table on exit (default: True).
- **custom_mapping** ([*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Optional dictionary mapping operations to custom FLOP counting functions.
- **skip_unsupported** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - If True, Higher Order Operators (HOPs) without registered FLOP
formulas are executed with a warning and tracked via
get_unsupported_ops() instead of failing (default: False).
Note that FLOPs of operations inside a skipped HOP are not
counted. Also required for Triton kernels to run at all: with
the default False a kernel (registered or not) is counted but
never executed, leaving its output buffer untouched. Regular
ops without formulas always execute and count 0 FLOPs
regardless of this setting.

Example usage:

```
mod = ...
inp = ...

with FlopCounterMode(display=False) as flop_counter:
 mod(inp).sum().backward()

total = flop_counter.get_total_flops()

# For models with custom kernels or unsupported operations
with FlopCounterMode(display=True, skip_unsupported=True) as flop_counter:
 output = model(input)
 total_flops = flop_counter.get_total_flops()
 # Check what operations were skipped
 unsupported = flop_counter.get_unsupported_ops()
 if unsupported:
 print(f"Warning: Could not count FLOPs for: {unsupported}")

# To register custom FLOP formulas for your operations
from torch.utils.flop_counter import register_flop_formula

@register_flop_formula(torch.ops.mylib.my_op)
def my_op_flops(x_shape, out_shape=None, **kwargs):
 return 0 # Return 0 for ops with negligible FLOPs, or calculate actual FLOPs

with FlopCounterMode(display=True) as flop_counter:
 result = torch.ops.mylib.my_op(x) # FLOPs will be counted using registered formula
```

See also

[`register_flop_formula()`](torch.utils.flop_counter.register_flop_formula.html#torch.utils.flop_counter.register_flop_formula): Register custom FLOP counting formulas for operations

get_flop_counts()[[source]](https://github.com/pytorch/pytorch/blob/dcd7ed975a6b090ec2bcf2360c28c9a263be8fe5/torch/utils/flop_counter.py#L1050)

Return the flop counts as a dictionary of dictionaries.

The outer
dictionary is keyed by module name, and the inner dictionary is keyed by
operation name.

Returns:

The flop counts as a dictionary.

Return type:

Dict[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Dict[Any, [int](https://docs.python.org/3/builtins/functions.html#int)]]

get_unsupported_ops()[[source]](https://github.com/pytorch/pytorch/blob/dcd7ed975a6b090ec2bcf2360c28c9a263be8fe5/torch/utils/flop_counter.py#L1041)

Return a Counter of unsupported operations encountered.

Returns:

A Counter mapping operation names to the number of times

they were encountered without a registered FLOP formula.

Return type:

Counter[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]