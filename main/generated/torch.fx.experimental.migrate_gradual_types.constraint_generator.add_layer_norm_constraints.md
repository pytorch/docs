# torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints

torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints(*input_dim*, *normalized_dim*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1504)

The constraints say that the type has the form: `[*, 1024, 1024]`
while the normalized_dim have the form `[1024, 1024]`.

Parameters:

- **input_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**DVar**]*) - Input shape of layer norm
- **normalized_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - normalized_dim parameter of the module instance

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*]