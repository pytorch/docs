# torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless

torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless(*symbool*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/symbolic_shapes.py#L2702)

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