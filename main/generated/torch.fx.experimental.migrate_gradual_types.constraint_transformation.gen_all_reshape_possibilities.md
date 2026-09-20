# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_all_reshape_possibilities

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_all_reshape_possibilities(*list_of_dims*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1023)

Consider all possibilities what the input dimensions could be (number or dynamic)
Then generate the appropriate constraints using multiplication or mod depending on the possibility
The possibilities we consider here are the cross product of being equal to dyn or not equal to dyn
for the input. Target is fixed because at most one dimension could be dyn.
We have different cases for this.

Parameters:

- **list_of_dims** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**DVar**]*) - The input list of dimensions
- **target** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)*[**DVar**|*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**_DynType**]*) - The tensor we want to reshape to

Return type:

*Constraint*

Returns: A disjunction of transformed reshape constraints