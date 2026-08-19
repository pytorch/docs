# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L181)

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

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]