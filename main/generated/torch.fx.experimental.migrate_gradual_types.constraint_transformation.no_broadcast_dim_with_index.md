# torch.fx.experimental.migrate_gradual_types.constraint_transformation.no_broadcast_dim_with_index

torch.fx.experimental.migrate_gradual_types.constraint_transformation.no_broadcast_dim_with_index(*d1*, *d2*, *d3*, *d4*, *i*)[[source]](https://github.com/pytorch/pytorch/blob/65c295bfa29161891e39b83fac63c4f5417ffdc2/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1188)

Parameters:

- **d1** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - input 1
- **d2** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - input 2
- **d3** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - simulated broadcasting for input 1
- **d4** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - simulated broadcasting for input 2
- **i** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - the rank of the resulting tensor addition

Return type:

*Constraint*

Returns: Constraints for when no broadcasting occurs