# torch.fx.experimental.migrate_gradual_types.constraint_transformation.create_equality_constraints_for_broadcasting

torch.fx.experimental.migrate_gradual_types.constraint_transformation.create_equality_constraints_for_broadcasting(*e1*, *e2*, *e11*, *e12*, *d1*, *d2*, *d11*, *d12*)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1247)

Create equality constraints for when no broadcasting occurs
:param e1: Input 1
:param e2: Input 2
:param e11: Broadcasted input 1
:param e12: Broadcasted input 2
:param d1: Variables that store dimensions for e1
:param d2: Variables that store dimensions for e2
:param d11: Variables that store dimensions for e11
:param d12: Variables that store dimensions for e22

Returns: Four equality constraints

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*BinConstraintT*]