# StatefulSymbolicContext

*class*torch.fx.experimental.symbolic_shapes.StatefulSymbolicContext(*dynamic_sizes*, *dynamic_strides=None*, *constraint_sizes=None*, *constraint_strides=None*, *specialize_on=None*, *view_base_context=None*, *shape_ids=None*, *unbacked_bounds=None*, ***, *tensor_source*, *shape_env_to_source_to_symbol_cache=<factory>*, *excluded_sizes=None*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/fx/experimental/symbolic_shapes.py#L2326)

Create symbols in `_create_symbolic_sizes_strides_storage_offset` via
a symbolic_context determination as given by a cache of Source:Symbol. A cache hit
will reuse a stored symbol, and a cache miss will write to this cache.

This behaves like StatelessSymbolicContext, except the cache supersedes the
other values - dynamic_sizes and constraint_sizes will not be read if we cache
hit.

It is the cache owner's responsibility to maintain the lifecycle of the cache
with respect to different shape_envs, clearing, etc.