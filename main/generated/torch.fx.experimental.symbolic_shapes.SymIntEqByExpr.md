# SymIntEqByExpr

*class*torch.fx.experimental.symbolic_shapes.SymIntEqByExpr(*val*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/symbolic_shapes.py#L273)

This is a wrapper around SymInt which has alternative semantics for
equality and pickling. Specifically, instead of erroring or guarding, we
instead will hash/compare equality based on the underlying sympy
expression; e.g., s0 and s1 will always compare as False.

NB: This does NOT do fancy analysis that maybe_evaluate_static does;
we can only reason through equalities that occur because to expressions
canonicalize to the same expression via regular simplification.