# torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr

torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/symbolic_shapes.py#L771)

Canonicalize a boolean expression by transforming it into a lt / le
inequality and moving all the non-constant terms to the rhs.
We canonicalize And / Ors / Not via cnf and then canonicalize their subexpr
recursively
nb. sympy.Rel.canonical is not good enough [sympy/sympy#25924](https://github.com/sympy/sympy/issues/25924)

Parameters:

**expr** (*sympy.Expr*) - Expression to canonicalize

Return type:

*_T*