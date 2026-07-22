# torch.fx.experimental.unify_refinements.substitute_all_types

torch.fx.experimental.unify_refinements.substitute_all_types(*graph*, *mapping*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/fx/experimental/unify_refinements.py#L109)

Apply the most general unifier to all types in a graph
till reaching a fixed point. If the input and output graph
are the same, we converge.