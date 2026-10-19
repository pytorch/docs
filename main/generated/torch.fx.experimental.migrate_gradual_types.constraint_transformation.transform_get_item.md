# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L181)

generate an equality of the form:
t = [a1, ..., an]
then generate constraints that check if the given index is valid
given this particular tensor size.
If the index is valid, generate a constraint to get the item
Note that we already handled the Dyn input case in the previous
step.
:param constraint: GetItem which assumes we are getting an item from a tensor (not Dyn)
:param counter: variable tracking

Returns: simplified constraints for GetItem

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/builtins/functions.html#int)]