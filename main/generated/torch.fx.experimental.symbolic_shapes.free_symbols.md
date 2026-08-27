# torch.fx.experimental.symbolic_shapes.free_symbols

torch.fx.experimental.symbolic_shapes.free_symbols(*val*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/symbolic_shapes.py#L1046)

Recursively collect all free symbols from a value.

This function traverses various data structures (tensors, lists, tuples, etc.) and extracts
all sympy symbols contained within them. It's useful for finding all symbolic variables
that a complex nested structure depends on.

Parameters:

**val** ([*SymInt*](../torch.html#torch.SymInt)*|*[*SymFloat*](../torch.html#torch.SymFloat)*|*[*SymBool*](../torch.html#torch.SymBool)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|**Basic**|*[*Tensor*](../tensors.html#torch.Tensor)*|*[*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)*[*[*SymInt*](../torch.html#torch.SymInt)*|*[*SymFloat*](../torch.html#torch.SymFloat)*|*[*SymBool*](../torch.html#torch.SymBool)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|**Basic**|*[*Tensor*](../tensors.html#torch.Tensor)*]*) - The value to extract symbols from. Can be a symbolic type (SymInt, SymFloat, SymBool),
a container (tuple, list), a tensor, or None.

Returns:

An ordered set of all free symbols found in the value.

Return type:

OrderedSet[sympy.Symbol]