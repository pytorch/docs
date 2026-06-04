# SubclassSymbolicContext

*class*torch.fx.experimental.symbolic_shapes.SubclassSymbolicContext(*dynamic_sizes*, *dynamic_strides=None*, *constraint_sizes=None*, *constraint_strides=None*, *specialize_on=None*, *view_base_context=None*, *shape_ids=None*, *unbacked_bounds=None*, *inner_contexts=<factory>*, *track_outer_size_stride=True*, ***, *tensor_source*, *shape_env_to_source_to_symbol_cache=<factory>*, *excluded_sizes=None*)[[source]](https://github.com/pytorch/pytorch/blob/40a42e9b743c053cc9e6d11c0502026a8f5d7d57/torch/fx/experimental/symbolic_shapes.py#L2357)

The correct symbolic context for a given inner tensor of a traceable tensor subclass
may differ from that of the outer symbolic context. This structure allows for this
flexibility, with inner symbolic contexts mapped via attr -> symbolic context.