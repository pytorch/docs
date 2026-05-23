# torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless

torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless(*symbool*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/fx/experimental/symbolic_shapes.py#L2675)

Converts a SymBool or bool to a SymInt or int without introducing guards.

This function maps True to 1 and False to 0, preserving the symbolic nature
of the input when it's a SymBool. Unlike regular casting which might introduce
guards, this function performs the conversion without adding any guards.

Parameters:

**symbool** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|*[*SymBool*](../torch.html#torch.SymBool)) - A boolean value, either a concrete bool or symbolic SymBool

Returns:

The corresponding integer value (1 for True, 0 for False) as either
a concrete int or symbolic SymInt

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | [*SymInt*](../torch.html#torch.SymInt)