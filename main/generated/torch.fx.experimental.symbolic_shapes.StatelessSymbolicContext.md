# StatelessSymbolicContext

*class*torch.fx.experimental.symbolic_shapes.StatelessSymbolicContext(*dynamic_sizes*, *dynamic_strides=None*, *constraint_sizes=None*, *constraint_strides=None*, *specialize_on=None*, *view_base_context=None*, *shape_ids=None*, *unbacked_bounds=None*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/fx/experimental/symbolic_shapes.py#L2272)

Create symbols in `_create_symbolic_sizes_strides_storage_offset` via
a symbolic_context determination as given by `DimDynamic` and `DimConstraint`.
This will cause fresh symbols to be allocated