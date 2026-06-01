# torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints

torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints(*input_dim*, *normalized_dim*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1504)

The constraints say that the type has the form: `[*, 1024, 1024]`
while the normalized_dim have the form `[1024, 1024]`.

Parameters:

- **input_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**DVar**]*) - Input shape of layer norm
- **normalized_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - normalized_dim parameter of the module instance

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*]