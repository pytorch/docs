# torch.fx.experimental.unify_refinements.substitute_all_types

torch.fx.experimental.unify_refinements.substitute_all_types(*graph*, *mapping*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/fx/experimental/unify_refinements.py#L109)

Apply the most general unifier to all types in a graph
till reaching a fixed point. If the input and output graph
are the same, we converge.