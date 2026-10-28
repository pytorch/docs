# torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints

torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints(*input_dim*, *normalized_dim*)[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1504)

The constraints say that the type has the form: `[*, 1024, 1024]`
while the normalized_dim have the form `[1024, 1024]`.

Parameters:

- **input_dim** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - Input shape of layer norm
- **normalized_dim** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - normalized_dim parameter of the module instance

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*]