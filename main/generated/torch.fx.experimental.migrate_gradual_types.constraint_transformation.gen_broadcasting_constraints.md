# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_broadcasting_constraints

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_broadcasting_constraints(*e1*, *e2*, *e11*, *e12*, *i*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1391)

Simulates broadcasting on e1 and e2 and returns the results
respectively in e11 and e12. Because of gradual types,
e1 and e2 may not be equal. Similarly, e11 and e12 may not
be equal. e11 and e12 should be guaranteed to be consistent
as they represent the shapes of the tensors to be added after
broadcasting.
:param e1: TVar representing the type of input 1
:param e2: TVar representing the type of input 2
:param e11: TVar representing the broadcasted input 1
:param e12: TVar representing the broadcasted input 2
:param i: The rank of the resulting type of addition
:param counter: for variable tracking

Returns: Simplified broadcasting constraints

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, *Constraint*, *Constraint*, [list](https://docs.python.org/3/library/stdtypes.html#list)[*BinConstraintD*], [int](https://docs.python.org/3/library/functions.html#int)]