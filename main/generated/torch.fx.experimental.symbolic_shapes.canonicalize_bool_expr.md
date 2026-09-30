# torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr

torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/fx/experimental/symbolic_shapes.py#L777)

Canonicalize supported boolean expressions recursively. Ge/Gt relations are
rewritten as Le/Lt, and relations with arithmetic operands are normalized by
subtraction. Relations with boolean operands are canonicalized structurally
without arithmetic. And / Or / Not expressions are first converted to CNF.
nb. sympy.Rel.canonical is not good enough [sympy/sympy#25924](https://github.com/sympy/sympy/issues/25924)

Parameters:

**expr** (*_T*) - Expression to canonicalize

Return type:

*_T*