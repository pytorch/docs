# torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr

torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/fx/experimental/symbolic_shapes.py#L777)

Canonicalize supported boolean expressions recursively. Ge/Gt relations are
rewritten as Le/Lt, and relations with arithmetic operands are normalized by
subtraction. Relations with boolean operands are canonicalized structurally
without arithmetic. And / Or / Not expressions are first converted to CNF.
nb. sympy.Rel.canonical is not good enough [sympy/sympy#25924](https://github.com/sympy/sympy/issues/25924)

Parameters:

**expr** (*_T*) - Expression to canonicalize

Return type:

*_T*