# torch.fx.experimental.unify_refinements.substitute_all_types

torch.fx.experimental.unify_refinements.substitute_all_types(*graph*, *mapping*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/unify_refinements.py#L109)

Apply the most general unifier to all types in a graph
till reaching a fixed point. If the input and output graph
are the same, we converge.