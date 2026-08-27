# torch.fx.experimental.symbolic_shapes.has_static_value

torch.fx.experimental.symbolic_shapes.has_static_value(*a*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/symbolic_shapes.py#L506)

User-code friendly utility to check if a value is static or dynamic.
Returns true if given a constant, or a symbolic expression with a fixed value.

Parameters:

**a** (*Union**[*[*SymBool*](../torch.html#torch.SymBool)*,*[*SymFloat*](../torch.html#torch.SymFloat)*,*[*SymInt*](../torch.html#torch.SymInt)*,*[*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Object to test

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)