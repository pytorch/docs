# torch.fx.experimental.migrate_gradual_types.constraint_generator.tensor_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.tensor_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L579)

If the tensor is a scalar, we will skip it since we
do not support scalars yet. We will add support in the future
if it's needed. For our examples so far, scalars are not needed.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]