# torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities

torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities(*my_list*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L969)

Generate all possibilities of being equal or not equal to dyn for my_list
:param my_list: List of tensor dimensions

Returns: A list of a list of constraints. Each list of constraints corresponds to
one possibility about the values of the dimension variables

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*BinConstraintD*, ...]]