# SymIntEqByExpr

*class*torch.fx.experimental.symbolic_shapes.SymIntEqByExpr(*val*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/fx/experimental/symbolic_shapes.py#L307)

This is a wrapper around SymInt which has alternative semantics for
equality and pickling. Specifically, instead of erroring or guarding, we
instead will hash/compare equality based on the underlying sympy
expression; e.g., s0 and s1 will always compare as False.

NB: This does NOT do fancy analysis that maybe_evaluate_static does;
we can only reason through equalities that occur because to expressions
canonicalize to the same expression via regular simplification.