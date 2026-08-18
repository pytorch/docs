# torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities

torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities(*my_list*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L969)

Generate all possibilities of being equal or not equal to dyn for my_list
:param my_list: List of tensor dimensions

Returns: A list of a list of constraints. Each list of constraints corresponds to
one possibility about the values of the dimension variables

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*BinConstraintD*, ...]]