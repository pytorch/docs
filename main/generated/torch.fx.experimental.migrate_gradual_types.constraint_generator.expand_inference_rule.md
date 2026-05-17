# torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L307)

We generate the exact constraints as we do for tensor additions but we constraint
the rank of this expression to be equal to len(n.args[1:]) so that only
those cases get considered for the output

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]