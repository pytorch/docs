# torch.fx.experimental.symbolic_shapes.has_static_value

torch.fx.experimental.symbolic_shapes.has_static_value(*a*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/fx/experimental/symbolic_shapes.py#L500)

User-code friendly utility to check if a value is static or dynamic.
Returns true if given a constant, or a symbolic expression with a fixed value.

Parameters:

**a** (*Union**[*[*SymBool*](../torch.html#torch.SymBool)*,*[*SymFloat*](../torch.html#torch.SymFloat)*,*[*SymInt*](../torch.html#torch.SymInt)*,*[*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Object to test

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)