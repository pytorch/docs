# torch.fx.experimental.unify_refinements.substitute_all_types

torch.fx.experimental.unify_refinements.substitute_all_types(*graph*, *mapping*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/unify_refinements.py#L109)

Apply the most general unifier to all types in a graph
till reaching a fixed point. If the input and output graph
are the same, we converge.