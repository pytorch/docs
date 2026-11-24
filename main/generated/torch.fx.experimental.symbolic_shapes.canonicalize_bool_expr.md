# torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr

torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/experimental/symbolic_shapes.py#L809)

Canonicalize supported boolean expressions recursively. Ge/Gt relations are
rewritten as Le/Lt, and relations with arithmetic operands are normalized by
subtraction. Relations with boolean operands are canonicalized structurally
without arithmetic. And / Or / Not expressions are first converted to CNF.
nb. sympy.Rel.canonical is not good enough [sympy/sympy#25924](https://github.com/sympy/sympy/issues/25924)

Parameters:

**expr** (*_T*) - Expression to canonicalize

Return type:

*_T*