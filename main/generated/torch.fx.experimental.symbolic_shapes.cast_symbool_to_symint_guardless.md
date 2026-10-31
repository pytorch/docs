# torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless

torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless(*symbool*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/fx/experimental/symbolic_shapes.py#L2703)

Converts a SymBool or bool to a SymInt or int without introducing guards.

This function maps True to 1 and False to 0, preserving the symbolic nature
of the input when it's a SymBool. Unlike regular casting which might introduce
guards, this function performs the conversion without adding any guards.

Parameters:

**symbool** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*|*[*SymBool*](../torch.html#torch.SymBool)) - A boolean value, either a concrete bool or symbolic SymBool

Returns:

The corresponding integer value (1 for True, 0 for False) as either
a concrete int or symbolic SymInt

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int) | [*SymInt*](../torch.html#torch.SymInt)