# DimConstraints

*class*torch.fx.experimental.symbolic_shapes.DimConstraints(*symbol_to_source*, *var_to_val*, *marked_dynamic*, *source_name_to_debug_name*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3001)

Custom solver for a system of constraints on symbolic dimensions.
Solutions are "static" values or simplified "dynamic" constraints.

add(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3167)

Add an expression to the set of constraints.

Return whether the expression is a trivial constraint (i.e., an obvious tautology).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

add_equality(*source*, *expr*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3217)

Add an equality constraint

forced_specializations()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3395)

Returns a dictionary of the names of symbols to their specialized value

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *Expr*]

prettify_results(*original_signature*, *dynamic_shapes*, *constraint_violation_error*, *forced_specializations*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3605)

Format a message for constraint violation errors

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

rewrite_with_congruences(*s*, *expr*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3068)

Eliminate expressions of the form b // d and b % d while adding congruences of the form b % d == k.
This leaves rational operators (in particular of the form b / d) that our inequality solver can handle.
We solve the added congruences separately (using our congruence solver, see below).

Return type:

*_SympyT*

solve()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L3280)

Solve the system of constraint equations to find simplified constraints