# DimConstraints

*class*torch.fx.experimental.symbolic_shapes.DimConstraints(*symbol_to_source*, *var_to_val*, *marked_dynamic*, *source_name_to_debug_name*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3020)

Custom solver for a system of constraints on symbolic dimensions.
Solutions are "static" values or simplified "dynamic" constraints.

add(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3186)

Add an expression to the set of constraints.

Return whether the expression is a trivial constraint (i.e., an obvious tautology).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

add_equality(*source*, *expr*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3236)

Add an equality constraint

forced_specializations()[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3414)

Returns a dictionary of the names of symbols to their specialized value

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *Expr*]

prettify_results(*original_signature*, *dynamic_shapes*, *constraint_violation_error*, *forced_specializations*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3624)

Format a message for constraint violation errors

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

rewrite_with_congruences(*s*, *expr*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3087)

Eliminate expressions of the form b // d and b % d while adding congruences of the form b % d == k.
This leaves rational operators (in particular of the form b / d) that our inequality solver can handle.
We solve the added congruences separately (using our congruence solver, see below).

Return type:

*_SympyT*

solve()[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/symbolic_shapes.py#L3299)

Solve the system of constraint equations to find simplified constraints