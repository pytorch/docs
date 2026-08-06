# torch.fx.experimental.symbolic_shapes.guard_scalar

torch.fx.experimental.symbolic_shapes.guard_scalar(*a*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/fx/experimental/symbolic_shapes.py#L1716)

Guard a scalar value, which can be a symbolic or concrete boolean, integer, or float.

This function dispatches to the appropriate guard function based on the type of the input.

Parameters:

**a** ([*SymBool*](../torch.html#torch.SymBool)*|*[*SymInt*](../torch.html#torch.SymInt)*|*[*SymFloat*](../torch.html#torch.SymFloat)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|*[*float*](https://docs.python.org/3/library/functions.html#float)) - A symbolic or concrete scalar value (bool, int, or float)

Returns:

The concrete value after guarding

Raises:

[**AssertionError**](https://docs.python.org/3/library/exceptions.html#AssertionError) - If the input is not a recognized scalar type

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float)