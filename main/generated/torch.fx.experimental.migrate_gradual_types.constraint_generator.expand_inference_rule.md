# torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L307)

We generate the exact constraints as we do for tensor additions but we constraint
the rank of this expression to be equal to len(n.args[1:]) so that only
those cases get considered for the output

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]