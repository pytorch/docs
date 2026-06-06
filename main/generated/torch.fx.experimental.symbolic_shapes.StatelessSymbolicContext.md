# StatelessSymbolicContext

*class*torch.fx.experimental.symbolic_shapes.StatelessSymbolicContext(*dynamic_sizes*, *dynamic_strides=None*, *constraint_sizes=None*, *constraint_strides=None*, *specialize_on=None*, *view_base_context=None*, *shape_ids=None*, *unbacked_bounds=None*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/fx/experimental/symbolic_shapes.py#L2251)

Create symbols in `_create_symbolic_sizes_strides_storage_offset` via
a symbolic_context determination as given by `DimDynamic` and `DimConstraint`.
This will cause fresh symbols to be allocated