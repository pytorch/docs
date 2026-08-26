# StatelessSymbolicContext

*class*torch.fx.experimental.symbolic_shapes.StatelessSymbolicContext(*dynamic_sizes*, *dynamic_strides=None*, *constraint_sizes=None*, *constraint_strides=None*, *specialize_on=None*, *view_base_context=None*, *shape_ids=None*, *unbacked_bounds=None*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/fx/experimental/symbolic_shapes.py#L2277)

Create symbols in `_create_symbolic_sizes_strides_storage_offset` via
a symbolic_context determination as given by `DimDynamic` and `DimConstraint`.
This will cause fresh symbols to be allocated