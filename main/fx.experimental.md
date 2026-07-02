# torch.fx.experimental

Warning

These APIs are experimental and subject to change without notice.

*class*torch.fx.experimental.sym_node.DynamicInt(*val*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/fx/experimental/sym_node.py#L667)

User API for marking dynamic integers in torch.compile.
Intended to be compatible with both compile and eager mode.

Example usage:

```
fn = torch.compile(f)
x = DynamicInt(4)
fn(x) # compiles x as a dynamic integer input; returns f(4)
```

Return type:

Self

## torch.fx.experimental.sym_node

| [`is_channels_last_contiguous_2d`](generated/torch.fx.experimental.sym_node.is_channels_last_contiguous_2d.html#torch.fx.experimental.sym_node.is_channels_last_contiguous_2d) | |
| --- | --- |
| [`is_channels_last_contiguous_3d`](generated/torch.fx.experimental.sym_node.is_channels_last_contiguous_3d.html#torch.fx.experimental.sym_node.is_channels_last_contiguous_3d) | |
| [`is_channels_last_strides_2d`](generated/torch.fx.experimental.sym_node.is_channels_last_strides_2d.html#torch.fx.experimental.sym_node.is_channels_last_strides_2d) | |
| [`is_channels_last_strides_3d`](generated/torch.fx.experimental.sym_node.is_channels_last_strides_3d.html#torch.fx.experimental.sym_node.is_channels_last_strides_3d) | |
| [`is_contiguous`](generated/torch.fx.experimental.sym_node.is_contiguous.html#torch.fx.experimental.sym_node.is_contiguous) | |
| [`is_non_overlapping_and_dense_indicator`](generated/torch.fx.experimental.sym_node.is_non_overlapping_and_dense_indicator.html#torch.fx.experimental.sym_node.is_non_overlapping_and_dense_indicator) | |
| [`method_to_operator`](generated/torch.fx.experimental.sym_node.method_to_operator.html#torch.fx.experimental.sym_node.method_to_operator) | |
| [`sympy_is_channels_last_contiguous_2d`](generated/torch.fx.experimental.sym_node.sympy_is_channels_last_contiguous_2d.html#torch.fx.experimental.sym_node.sympy_is_channels_last_contiguous_2d) | |
| [`sympy_is_channels_last_contiguous_3d`](generated/torch.fx.experimental.sym_node.sympy_is_channels_last_contiguous_3d.html#torch.fx.experimental.sym_node.sympy_is_channels_last_contiguous_3d) | |
| [`sympy_is_channels_last_strides_2d`](generated/torch.fx.experimental.sym_node.sympy_is_channels_last_strides_2d.html#torch.fx.experimental.sym_node.sympy_is_channels_last_strides_2d) | |
| [`sympy_is_channels_last_strides_3d`](generated/torch.fx.experimental.sym_node.sympy_is_channels_last_strides_3d.html#torch.fx.experimental.sym_node.sympy_is_channels_last_strides_3d) | |
| [`sympy_is_channels_last_strides_generic`](generated/torch.fx.experimental.sym_node.sympy_is_channels_last_strides_generic.html#torch.fx.experimental.sym_node.sympy_is_channels_last_strides_generic) | |
| [`sympy_is_contiguous`](generated/torch.fx.experimental.sym_node.sympy_is_contiguous.html#torch.fx.experimental.sym_node.sympy_is_contiguous) | |
| [`sympy_is_contiguous_generic`](generated/torch.fx.experimental.sym_node.sympy_is_contiguous_generic.html#torch.fx.experimental.sym_node.sympy_is_contiguous_generic) | |
| [`to_node`](generated/torch.fx.experimental.sym_node.to_node.html#torch.fx.experimental.sym_node.to_node) | |

## torch.fx.experimental.symbolic_shapes

| [`ShapeEnv`](generated/torch.fx.experimental.symbolic_shapes.ShapeEnv.html#torch.fx.experimental.symbolic_shapes.ShapeEnv) | |
| --- | --- |
| [`DimDynamic`](generated/torch.fx.experimental.symbolic_shapes.DimDynamic.html#torch.fx.experimental.symbolic_shapes.DimDynamic) | Controls how to perform symbol allocation for a dimension. |
| [`StrictMinMaxConstraint`](generated/torch.fx.experimental.symbolic_shapes.StrictMinMaxConstraint.html#torch.fx.experimental.symbolic_shapes.StrictMinMaxConstraint) | For clients: the size at this dimension must be within 'vr' (which specifies a lower and upper bound, inclusive-inclusive) AND it must be non-negative and should not be 0 or 1 (but see NB below). |
| [`RelaxedUnspecConstraint`](generated/torch.fx.experimental.symbolic_shapes.RelaxedUnspecConstraint.html#torch.fx.experimental.symbolic_shapes.RelaxedUnspecConstraint) | For clients: no explicit constraint; constraint is whatever is implicitly inferred by guards from tracing. |
| [`EqualityConstraint`](generated/torch.fx.experimental.symbolic_shapes.EqualityConstraint.html#torch.fx.experimental.symbolic_shapes.EqualityConstraint) | Represent and decide various kinds of equality constraints between input sources. |
| [`SymbolicContext`](generated/torch.fx.experimental.symbolic_shapes.SymbolicContext.html#torch.fx.experimental.symbolic_shapes.SymbolicContext) | Data structure specifying how we should create symbols in `_create_symbolic_sizes_strides_storage_offset`; e.g., should they be static or dynamic. |
| [`StatelessSymbolicContext`](generated/torch.fx.experimental.symbolic_shapes.StatelessSymbolicContext.html#torch.fx.experimental.symbolic_shapes.StatelessSymbolicContext) | Create symbols in `_create_symbolic_sizes_strides_storage_offset` via a symbolic_context determination as given by `DimDynamic` and `DimConstraint`. |
| [`StatefulSymbolicContext`](generated/torch.fx.experimental.symbolic_shapes.StatefulSymbolicContext.html#torch.fx.experimental.symbolic_shapes.StatefulSymbolicContext) | Create symbols in `_create_symbolic_sizes_strides_storage_offset` via a symbolic_context determination as given by a cache of Source:Symbol. |
| [`SubclassSymbolicContext`](generated/torch.fx.experimental.symbolic_shapes.SubclassSymbolicContext.html#torch.fx.experimental.symbolic_shapes.SubclassSymbolicContext) | The correct symbolic context for a given inner tensor of a traceable tensor subclass may differ from that of the outer symbolic context. |
| [`SymIntEqByExpr`](generated/torch.fx.experimental.symbolic_shapes.SymIntEqByExpr.html#torch.fx.experimental.symbolic_shapes.SymIntEqByExpr) | This is a wrapper around SymInt which has alternative semantics for equality and pickling. |
| [`SymIntSymbolicContext`](generated/torch.fx.experimental.symbolic_shapes.SymIntSymbolicContext.html#torch.fx.experimental.symbolic_shapes.SymIntSymbolicContext) | Data structure specifying any constraints on a SymInt input |
| [`TrackedFake`](generated/torch.fx.experimental.symbolic_shapes.TrackedFake.html#torch.fx.experimental.symbolic_shapes.TrackedFake) | Tracks the sources of all fake tensors we wrap in Dynamo. |
| [`ValueRangesSLoc`](generated/torch.fx.experimental.symbolic_shapes.ValueRangesSLoc.html#torch.fx.experimental.symbolic_shapes.ValueRangesSLoc) | Locations of the guards that triggered lower and upper bound. |
| [`DimConstraints`](generated/torch.fx.experimental.symbolic_shapes.DimConstraints.html#torch.fx.experimental.symbolic_shapes.DimConstraints) | Custom solver for a system of constraints on symbolic dimensions. |
| [`ShapeEnvSettings`](generated/torch.fx.experimental.symbolic_shapes.ShapeEnvSettings.html#torch.fx.experimental.symbolic_shapes.ShapeEnvSettings) | Encapsulates all shape env settings that could potentially affect FakeTensor dispatch. |
| [`ConvertIntKey`](generated/torch.fx.experimental.symbolic_shapes.ConvertIntKey.html#torch.fx.experimental.symbolic_shapes.ConvertIntKey) | |
| [`CallMethodKey`](generated/torch.fx.experimental.symbolic_shapes.CallMethodKey.html#torch.fx.experimental.symbolic_shapes.CallMethodKey) | |
| [`PropagateUnbackedSymInts`](generated/torch.fx.experimental.symbolic_shapes.PropagateUnbackedSymInts.html#torch.fx.experimental.symbolic_shapes.PropagateUnbackedSymInts) | |
| [`DivideByKey`](generated/torch.fx.experimental.symbolic_shapes.DivideByKey.html#torch.fx.experimental.symbolic_shapes.DivideByKey) | |
| [`InnerTensorKey`](generated/torch.fx.experimental.symbolic_shapes.InnerTensorKey.html#torch.fx.experimental.symbolic_shapes.InnerTensorKey) | |
| [`Specialization`](generated/torch.fx.experimental.symbolic_shapes.Specialization.html#torch.fx.experimental.symbolic_shapes.Specialization) | This class is used in multi-graph compilation contexts where we generate multiple specialized graphs and dispatch to the appropriate one at runtime. |
| [`is_concrete_int`](generated/torch.fx.experimental.symbolic_shapes.is_concrete_int.html#torch.fx.experimental.symbolic_shapes.is_concrete_int) | Utility to check if underlying object in SymInt is concrete value. |
| [`is_concrete_bool`](generated/torch.fx.experimental.symbolic_shapes.is_concrete_bool.html#torch.fx.experimental.symbolic_shapes.is_concrete_bool) | Utility to check if underlying object in SymBool is concrete value. |
| [`is_concrete_float`](generated/torch.fx.experimental.symbolic_shapes.is_concrete_float.html#torch.fx.experimental.symbolic_shapes.is_concrete_float) | Utility to check if underlying object in SymInt is concrete value. |
| [`has_free_symbols`](generated/torch.fx.experimental.symbolic_shapes.has_free_symbols.html#torch.fx.experimental.symbolic_shapes.has_free_symbols) | Faster version of bool(free_symbols(val)) |
| [`has_free_unbacked_symbols`](generated/torch.fx.experimental.symbolic_shapes.has_free_unbacked_symbols.html#torch.fx.experimental.symbolic_shapes.has_free_unbacked_symbols) | Faster version of bool(free_unbacked_symbols(val)) |
| [`guard_or_true`](generated/torch.fx.experimental.symbolic_shapes.guard_or_true.html#torch.fx.experimental.symbolic_shapes.guard_or_true) | Try to guard a, if data dependent error encountered just return true. |
| [`guard_or_false`](generated/torch.fx.experimental.symbolic_shapes.guard_or_false.html#torch.fx.experimental.symbolic_shapes.guard_or_false) | Try to guard a, if data dependent error encountered just return false. |
| [`guard_size_oblivious`](generated/torch.fx.experimental.symbolic_shapes.guard_size_oblivious.html#torch.fx.experimental.symbolic_shapes.guard_size_oblivious) | Perform a guard on a symbolic boolean expression in a size oblivious way. |
| [`sym_and`](generated/torch.fx.experimental.symbolic_shapes.sym_and.html#torch.fx.experimental.symbolic_shapes.sym_and) | and, but for symbolic expressions, without bool casting. |
| [`sym_eq`](generated/torch.fx.experimental.symbolic_shapes.sym_eq.html#torch.fx.experimental.symbolic_shapes.sym_eq) | Like ==, but when run on list/tuple, it will recursively test equality and use sym_and to join the results together, without guarding. |
| [`sym_or`](generated/torch.fx.experimental.symbolic_shapes.sym_or.html#torch.fx.experimental.symbolic_shapes.sym_or) | or, but for symbolic expressions, without bool casting. |
| [`constrain_range`](generated/torch.fx.experimental.symbolic_shapes.constrain_range.html#torch.fx.experimental.symbolic_shapes.constrain_range) | Applies a constraint that the passed in SymInt must lie between min-max inclusive-inclusive, WITHOUT introducing a guard on the SymInt (meaning that it can be used on unbacked SymInts). |
| [`constrain_unify`](generated/torch.fx.experimental.symbolic_shapes.constrain_unify.html#torch.fx.experimental.symbolic_shapes.constrain_unify) | Given two SymInts, constrain them so that they must be equal. |
| [`canonicalize_bool_expr`](generated/torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr.html#torch.fx.experimental.symbolic_shapes.canonicalize_bool_expr) | Canonicalize a boolean expression by transforming it into a lt / le inequality and moving all the non-constant terms to the rhs. |
| [`statically_known_true`](generated/torch.fx.experimental.symbolic_shapes.statically_known_true.html#torch.fx.experimental.symbolic_shapes.statically_known_true) | Returns True if x can be simplified to a constant and is true. |
| [`statically_known_false`](generated/torch.fx.experimental.symbolic_shapes.statically_known_false.html#torch.fx.experimental.symbolic_shapes.statically_known_false) | Returns True if x can be simplified to a constant and is False. |
| [`has_static_value`](generated/torch.fx.experimental.symbolic_shapes.has_static_value.html#torch.fx.experimental.symbolic_shapes.has_static_value) | User-code friendly utility to check if a value is static or dynamic. |
| [`lru_cache`](generated/torch.fx.experimental.symbolic_shapes.lru_cache.html#torch.fx.experimental.symbolic_shapes.lru_cache) | |
| [`check_consistent`](generated/torch.fx.experimental.symbolic_shapes.check_consistent.html#torch.fx.experimental.symbolic_shapes.check_consistent) | Test that two "meta" values (typically either Tensor or SymInt) have the same values, e.g., after retracing. |
| [`compute_unbacked_bindings`](generated/torch.fx.experimental.symbolic_shapes.compute_unbacked_bindings.html#torch.fx.experimental.symbolic_shapes.compute_unbacked_bindings) | After having run fake tensor propagation and producing example_value result, traverse example_value looking for freshly bound unbacked symbols and record their paths for later. |
| [`rebind_unbacked`](generated/torch.fx.experimental.symbolic_shapes.rebind_unbacked.html#torch.fx.experimental.symbolic_shapes.rebind_unbacked) | Suppose we are retracing a pre-existing FX graph that previously had fake tensor propagation (and therefore unbacked SymInts). |
| [`resolve_unbacked_bindings`](generated/torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings.html#torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings) | When we do fake tensor prop, we oftentimes will allocate new unbacked symints. |
| [`is_accessor_node`](generated/torch.fx.experimental.symbolic_shapes.is_accessor_node.html#torch.fx.experimental.symbolic_shapes.is_accessor_node) | Helper function to determine if a node is trying to access a symbolic integer such as size, stride, offset or item. |
| [`cast_symbool_to_symint_guardless`](generated/torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless.html#torch.fx.experimental.symbolic_shapes.cast_symbool_to_symint_guardless) | Converts a SymBool or bool to a SymInt or int without introducing guards. |
| [`create_contiguous`](generated/torch.fx.experimental.symbolic_shapes.create_contiguous.html#torch.fx.experimental.symbolic_shapes.create_contiguous) | |
| [`error`](generated/torch.fx.experimental.symbolic_shapes.error.html#torch.fx.experimental.symbolic_shapes.error) | |
| [`eval_guards`](generated/torch.fx.experimental.symbolic_shapes.eval_guards.html#torch.fx.experimental.symbolic_shapes.eval_guards) | |
| [`eval_is_non_overlapping_and_dense`](generated/torch.fx.experimental.symbolic_shapes.eval_is_non_overlapping_and_dense.html#torch.fx.experimental.symbolic_shapes.eval_is_non_overlapping_and_dense) | |
| [`find_symbol_binding_fx_nodes`](generated/torch.fx.experimental.symbolic_shapes.find_symbol_binding_fx_nodes.html#torch.fx.experimental.symbolic_shapes.find_symbol_binding_fx_nodes) | Find all nodes in an FX graph that bind sympy Symbols. |
| [`free_symbols`](generated/torch.fx.experimental.symbolic_shapes.free_symbols.html#torch.fx.experimental.symbolic_shapes.free_symbols) | Recursively collect all free symbols from a value. |
| [`free_unbacked_symbols`](generated/torch.fx.experimental.symbolic_shapes.free_unbacked_symbols.html#torch.fx.experimental.symbolic_shapes.free_unbacked_symbols) | Like free_symbols, but filtered to only report unbacked symbols |
| [`fx_placeholder_targets`](generated/torch.fx.experimental.symbolic_shapes.fx_placeholder_targets.html#torch.fx.experimental.symbolic_shapes.fx_placeholder_targets) | |
| [`fx_placeholder_vals`](generated/torch.fx.experimental.symbolic_shapes.fx_placeholder_vals.html#torch.fx.experimental.symbolic_shapes.fx_placeholder_vals) | |
| [`guard_bool`](generated/torch.fx.experimental.symbolic_shapes.guard_bool.html#torch.fx.experimental.symbolic_shapes.guard_bool) | |
| [`guard_float`](generated/torch.fx.experimental.symbolic_shapes.guard_float.html#torch.fx.experimental.symbolic_shapes.guard_float) | |
| [`guard_int`](generated/torch.fx.experimental.symbolic_shapes.guard_int.html#torch.fx.experimental.symbolic_shapes.guard_int) | |
| [`guard_scalar`](generated/torch.fx.experimental.symbolic_shapes.guard_scalar.html#torch.fx.experimental.symbolic_shapes.guard_scalar) | Guard a scalar value, which can be a symbolic or concrete boolean, integer, or float. |
| [`guarding_hint_or_throw`](generated/torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw.html#torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw) | Return a concrete hint for a symbolic value, for use in guarding decisions. |
| [`has_guarding_hint`](generated/torch.fx.experimental.symbolic_shapes.has_guarding_hint.html#torch.fx.experimental.symbolic_shapes.has_guarding_hint) | Check if a symbolic value has a hint available for guarding. |
| [`has_symbolic_sizes_strides`](generated/torch.fx.experimental.symbolic_shapes.has_symbolic_sizes_strides.html#torch.fx.experimental.symbolic_shapes.has_symbolic_sizes_strides) | |
| [`is_nested_int`](generated/torch.fx.experimental.symbolic_shapes.is_nested_int.html#torch.fx.experimental.symbolic_shapes.is_nested_int) | |
| [`is_symbol_binding_fx_node`](generated/torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node.html#torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node) | Check if a given FX node is a symbol binding node. |
| [`is_symbolic`](generated/torch.fx.experimental.symbolic_shapes.is_symbolic.html#torch.fx.experimental.symbolic_shapes.is_symbolic) | |
| [`optimization_hint`](generated/torch.fx.experimental.symbolic_shapes.optimization_hint.html#torch.fx.experimental.symbolic_shapes.optimization_hint) | Return a concrete hint for a symbolic integer, for use in optimization decisions. |
| [`expect_true`](generated/torch.fx.experimental.symbolic_shapes.expect_true.html#torch.fx.experimental.symbolic_shapes.expect_true) | |
| [`log_lru_cache_stats`](generated/torch.fx.experimental.symbolic_shapes.log_lru_cache_stats.html#torch.fx.experimental.symbolic_shapes.log_lru_cache_stats) | |

## torch.fx.experimental.proxy_tensor

| [`make_fx`](generated/torch.fx.experimental.proxy_tensor.make_fx.html#torch.fx.experimental.proxy_tensor.make_fx) | Given a function f, return a new function which when executed with valid arguments to f, returns an FX GraphModule representing the set of operations that were executed during the course of execution. |
| --- | --- |
| [`handle_sym_dispatch`](generated/torch.fx.experimental.proxy_tensor.handle_sym_dispatch.html#torch.fx.experimental.proxy_tensor.handle_sym_dispatch) | Call into the currently active proxy tracing mode to do a SymInt/SymFloat/SymBool dispatch trace on a function that operates on these arguments. |
| [`get_innermost_proxy_mode`](generated/torch.fx.experimental.proxy_tensor.get_innermost_proxy_mode.html#torch.fx.experimental.proxy_tensor.get_innermost_proxy_mode) | |
| [`get_proxy_mode`](generated/torch.fx.experimental.proxy_tensor.get_proxy_mode.html#torch.fx.experimental.proxy_tensor.get_proxy_mode) | Current the currently active proxy tracing mode, or None if we are not currently tracing. |
| [`maybe_enable_thunkify`](generated/torch.fx.experimental.proxy_tensor.maybe_enable_thunkify.html#torch.fx.experimental.proxy_tensor.maybe_enable_thunkify) | Within this context manager, if you are doing make_fx tracing, we will thunkify all SymNode compute and avoid tracing it into the graph unless it is actually needed. |
| [`maybe_disable_thunkify`](generated/torch.fx.experimental.proxy_tensor.maybe_disable_thunkify.html#torch.fx.experimental.proxy_tensor.maybe_disable_thunkify) | Within a context, disable thunkification. |
| [`selective_decompose`](generated/torch.fx.experimental.proxy_tensor.selective_decompose.html#torch.fx.experimental.proxy_tensor.selective_decompose) | Retrace a joint graph module and selectively apply decomposition. |
| [`thunkify`](generated/torch.fx.experimental.proxy_tensor.thunkify.html#torch.fx.experimental.proxy_tensor.thunkify) | Delays computation of f until it's called again Also caches the result |
| [`track_tensor`](generated/torch.fx.experimental.proxy_tensor.track_tensor.html#torch.fx.experimental.proxy_tensor.track_tensor) | |
| [`track_tensor_tree`](generated/torch.fx.experimental.proxy_tensor.track_tensor_tree.html#torch.fx.experimental.proxy_tensor.track_tensor_tree) | |
| [`decompose`](generated/torch.fx.experimental.proxy_tensor.decompose.html#torch.fx.experimental.proxy_tensor.decompose) | |
| [`disable_autocast_cache`](generated/torch.fx.experimental.proxy_tensor.disable_autocast_cache.html#torch.fx.experimental.proxy_tensor.disable_autocast_cache) | |
| [`disable_proxy_modes_tracing`](generated/torch.fx.experimental.proxy_tensor.disable_proxy_modes_tracing.html#torch.fx.experimental.proxy_tensor.disable_proxy_modes_tracing) | |
| [`dispatch_trace`](generated/torch.fx.experimental.proxy_tensor.dispatch_trace.html#torch.fx.experimental.proxy_tensor.dispatch_trace) | |
| [`extract_val`](generated/torch.fx.experimental.proxy_tensor.extract_val.html#torch.fx.experimental.proxy_tensor.extract_val) | |
| [`fake_signature`](generated/torch.fx.experimental.proxy_tensor.fake_signature.html#torch.fx.experimental.proxy_tensor.fake_signature) | FX gets confused by varargs, de-confuse it |
| [`fetch_object_proxy`](generated/torch.fx.experimental.proxy_tensor.fetch_object_proxy.html#torch.fx.experimental.proxy_tensor.fetch_object_proxy) | |
| [`fetch_sym_proxy`](generated/torch.fx.experimental.proxy_tensor.fetch_sym_proxy.html#torch.fx.experimental.proxy_tensor.fetch_sym_proxy) | |
| [`has_proxy_slot`](generated/torch.fx.experimental.proxy_tensor.has_proxy_slot.html#torch.fx.experimental.proxy_tensor.has_proxy_slot) | |
| [`is_sym_node`](generated/torch.fx.experimental.proxy_tensor.is_sym_node.html#torch.fx.experimental.proxy_tensor.is_sym_node) | |
| [`maybe_handle_decomp`](generated/torch.fx.experimental.proxy_tensor.maybe_handle_decomp.html#torch.fx.experimental.proxy_tensor.maybe_handle_decomp) | |
| [`proxy_call`](generated/torch.fx.experimental.proxy_tensor.proxy_call.html#torch.fx.experimental.proxy_tensor.proxy_call) | |
| [`set_meta`](generated/torch.fx.experimental.proxy_tensor.set_meta.html#torch.fx.experimental.proxy_tensor.set_meta) | |
| [`set_original_aten_op`](generated/torch.fx.experimental.proxy_tensor.set_original_aten_op.html#torch.fx.experimental.proxy_tensor.set_original_aten_op) | |
| [`set_proxy_slot`](generated/torch.fx.experimental.proxy_tensor.set_proxy_slot.html#torch.fx.experimental.proxy_tensor.set_proxy_slot) | |
| [`snapshot_fake`](generated/torch.fx.experimental.proxy_tensor.snapshot_fake.html#torch.fx.experimental.proxy_tensor.snapshot_fake) | |

## torch.fx.experimental.optimization

| [`extract_subgraph`](generated/torch.fx.experimental.optimization.extract_subgraph.html#torch.fx.experimental.optimization.extract_subgraph) | Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph. |
| --- | --- |
| [`gen_mkl_autotuner`](generated/torch.fx.experimental.optimization.gen_mkl_autotuner.html#torch.fx.experimental.optimization.gen_mkl_autotuner) | This generates a heuristic that can be passed into optimize_for_inference that determines whether a subgraph should be run in MKL by running it with the example_inputs. |
| [`matches_module_pattern`](generated/torch.fx.experimental.optimization.matches_module_pattern.html#torch.fx.experimental.optimization.matches_module_pattern) | |
| [`modules_to_mkldnn`](generated/torch.fx.experimental.optimization.modules_to_mkldnn.html#torch.fx.experimental.optimization.modules_to_mkldnn) | For each node, if it's a module that can be preconverted into MKLDNN, then we do so and create a mapping to allow us to convert from the MKLDNN version of the module to the original. |
| [`optimize_for_inference`](generated/torch.fx.experimental.optimization.optimize_for_inference.html#torch.fx.experimental.optimization.optimize_for_inference) | Performs a set of optimization passes to optimize a model for the purposes of inference. |
| [`remove_dropout`](generated/torch.fx.experimental.optimization.remove_dropout.html#torch.fx.experimental.optimization.remove_dropout) | Removes all dropout layers from the module. |
| [`replace_node_module`](generated/torch.fx.experimental.optimization.replace_node_module.html#torch.fx.experimental.optimization.replace_node_module) | |
| [`reset_modules`](generated/torch.fx.experimental.optimization.reset_modules.html#torch.fx.experimental.optimization.reset_modules) | Maps each module that's been changed with modules_to_mkldnn back to its original. |
| [`use_mkl_length`](generated/torch.fx.experimental.optimization.use_mkl_length.html#torch.fx.experimental.optimization.use_mkl_length) | This is a heuristic that can be passed into optimize_for_inference that determines whether a subgraph should be run in MKL by checking if there are more than 2 nodes in it |

## torch.fx.experimental.recording

| [`record_shapeenv_event`](generated/torch.fx.experimental.recording.record_shapeenv_event.html#torch.fx.experimental.recording.record_shapeenv_event) | |
| --- | --- |
| [`replay_shape_env_events`](generated/torch.fx.experimental.recording.replay_shape_env_events.html#torch.fx.experimental.recording.replay_shape_env_events) | |
| [`shape_env_check_state_equal`](generated/torch.fx.experimental.recording.shape_env_check_state_equal.html#torch.fx.experimental.recording.shape_env_check_state_equal) | |

## torch.fx.experimental.unification.core

| [`reify`](generated/torch.fx.experimental.unification.core.reify.html#torch.fx.experimental.unification.core.reify) | Replace variables of expression with substitution >>> x, y = var(), var() >>> e = (1, x, (3, y)) >>> s = {x: 2, y: 4} >>> reify(e, s) (1, 2, (3, 4)) >>> e = {1: x, 3: (y, 5)} >>> reify(e, s) {1: 2, 3: (4, 5)} |
| --- | --- |

## torch.fx.experimental.unification.multipledispatch.utils

| [`typename`](generated/torch.fx.experimental.unification.multipledispatch.utils.typename.html#torch.fx.experimental.unification.multipledispatch.utils.typename) | Get the name of type. |
| --- | --- |
| [`expand_tuples`](generated/torch.fx.experimental.unification.multipledispatch.utils.expand_tuples.html#torch.fx.experimental.unification.multipledispatch.utils.expand_tuples) | ``` >>> expand_tuples([1, (2, 3)]) ``` |
| [`groupby`](generated/torch.fx.experimental.unification.multipledispatch.utils.groupby.html#torch.fx.experimental.unification.multipledispatch.utils.groupby) | Group a collection by a key function >>> names = ["Alice", "Bob", "Charlie", "Dan", "Edith", "Frank"] >>> groupby(len, names) # doctest: +SKIP {3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']} >>> iseven = lambda x: x % 2 == 0 >>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8]) # doctest: +SKIP {False: [1, 3, 5, 7], True: [2, 4, 6, 8]} . |
| [`raises`](generated/torch.fx.experimental.unification.multipledispatch.utils.raises.html#torch.fx.experimental.unification.multipledispatch.utils.raises) | |
| [`reverse_dict`](generated/torch.fx.experimental.unification.multipledispatch.utils.reverse_dict.html#torch.fx.experimental.unification.multipledispatch.utils.reverse_dict) | Reverses direction of dependence dict. |

## torch.fx.experimental.unification.unification_tools

| [`assoc`](generated/torch.fx.experimental.unification.unification_tools.assoc.html#torch.fx.experimental.unification.unification_tools.assoc) | Return a new dict with new key value pair |
| --- | --- |
| [`assoc_in`](generated/torch.fx.experimental.unification.unification_tools.assoc_in.html#torch.fx.experimental.unification.unification_tools.assoc_in) | Return a new dict with new, potentially nested, key value pair |
| [`dissoc`](generated/torch.fx.experimental.unification.unification_tools.dissoc.html#torch.fx.experimental.unification.unification_tools.dissoc) | Return a new dict with the given key(s) removed. |
| [`first`](generated/torch.fx.experimental.unification.unification_tools.first.html#torch.fx.experimental.unification.unification_tools.first) | The first element in a sequence |
| [`get_in`](generated/torch.fx.experimental.unification.unification_tools.get_in.html#torch.fx.experimental.unification.unification_tools.get_in) | Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys. |
| [`groupby`](generated/torch.fx.experimental.unification.unification_tools.groupby.html#torch.fx.experimental.unification.unification_tools.groupby) | Group a collection by a key function |
| [`keyfilter`](generated/torch.fx.experimental.unification.unification_tools.keyfilter.html#torch.fx.experimental.unification.unification_tools.keyfilter) | Filter items in dictionary by key |
| [`keymap`](generated/torch.fx.experimental.unification.unification_tools.keymap.html#torch.fx.experimental.unification.unification_tools.keymap) | Apply function to keys of dictionary |
| [`merge`](generated/torch.fx.experimental.unification.unification_tools.merge.html#torch.fx.experimental.unification.unification_tools.merge) | Merge a collection of dictionaries |
| [`merge_with`](generated/torch.fx.experimental.unification.unification_tools.merge_with.html#torch.fx.experimental.unification.unification_tools.merge_with) | Merge dictionaries and apply function to combined values |
| [`update_in`](generated/torch.fx.experimental.unification.unification_tools.update_in.html#torch.fx.experimental.unification.unification_tools.update_in) | Update value in a (potentially) nested dictionary |
| [`valfilter`](generated/torch.fx.experimental.unification.unification_tools.valfilter.html#torch.fx.experimental.unification.unification_tools.valfilter) | Filter items in dictionary by value |
| [`valmap`](generated/torch.fx.experimental.unification.unification_tools.valmap.html#torch.fx.experimental.unification.unification_tools.valmap) | Apply function to values of dictionary |
| [`itemfilter`](generated/torch.fx.experimental.unification.unification_tools.itemfilter.html#torch.fx.experimental.unification.unification_tools.itemfilter) | Filter items in dictionary by item |
| [`itemmap`](generated/torch.fx.experimental.unification.unification_tools.itemmap.html#torch.fx.experimental.unification.unification_tools.itemmap) | Apply function to items of dictionary |

## torch.fx.experimental.migrate_gradual_types.transform_to_z3

| [`transform_algebraic_expression`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_algebraic_expression.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_algebraic_expression) | Transforms an algebraic expression to z3 format :param expr: An expression is either a dimension variable or an algebraic-expression |
| --- | --- |
| [`transform_all_constraints`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints) | Given a trace, generates constraints and transforms them to z3 format |
| [`transform_all_constraints_trace_time`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints_trace_time.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints_trace_time) | Takes a node and a graph and generates two sets of constraints. |
| [`transform_dimension`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension) | Takes a dimension variable or a number and transforms it to a tuple according to our scheme :param dimension: The dimension to be transformed :param counter: variable tracking |
| [`transform_to_z3`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_to_z3.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_to_z3) | |
| [`transform_var`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var) | Transforms tensor variables to a format understood by z3 :param tensor: Tensor variable or a tensor type potentially with variable dimensions |
| [`evaluate_conditional_with_constraints`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.evaluate_conditional_with_constraints.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.evaluate_conditional_with_constraints) | Given an IR and a node representing a conditional, evaluate the conditional and its negation :param tracer_root: Tracer root for module instances :param node: The node to be evaluated |
| [`iterate_till_fixed_point`](generated/torch.fx.experimental.migrate_gradual_types.transform_to_z3.iterate_till_fixed_point.html#torch.fx.experimental.migrate_gradual_types.transform_to_z3.iterate_till_fixed_point) | Transform constraints till reaching a fixed point |

## torch.fx.experimental.migrate_gradual_types.constraint

| [`is_algebraic_expression`](generated/torch.fx.experimental.migrate_gradual_types.constraint.is_algebraic_expression.html#torch.fx.experimental.migrate_gradual_types.constraint.is_algebraic_expression) | |
| --- | --- |
| [`is_bool_expr`](generated/torch.fx.experimental.migrate_gradual_types.constraint.is_bool_expr.html#torch.fx.experimental.migrate_gradual_types.constraint.is_bool_expr) | |
| [`is_dim`](generated/torch.fx.experimental.migrate_gradual_types.constraint.is_dim.html#torch.fx.experimental.migrate_gradual_types.constraint.is_dim) | |

## torch.fx.experimental.migrate_gradual_types.constraint_generator

| [`adaptive_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.adaptive_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.adaptive_inference_rule) | |
| --- | --- |
| [`add_layer_norm_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.add_layer_norm_constraints) | The constraints say that the type has the form: `[*, 1024, 1024]` while the normalized_dim have the form `[1024, 1024]`. |
| [`add_linear_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.add_linear_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.add_linear_constraints) | |
| [`arange_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.arange_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.arange_inference_rule) | |
| [`assert_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.assert_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.assert_inference_rule) | |
| [`batchnorm_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.batchnorm_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.batchnorm_inference_rule) | |
| [`bmm_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule) | Constraints that match the input to a size 3 tensor and switch the dimensions according to the rules of batch multiplication |
| [`broadcasting_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.broadcasting_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.broadcasting_inference_rule) | |
| [`conv2d_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.conv2d_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.conv2d_inference_rule) | |
| [`cumsum_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule) | Input and output shapes should be equal We should verify that the index is valid |
| [`embedding_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.embedding_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.embedding_inference_rule) | The output shape differs from the input shape in the last dimension |
| [`embedding_inference_rule_functional`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.embedding_inference_rule_functional.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.embedding_inference_rule_functional) | |
| [`eq_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.eq_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.eq_inference_rule) | |
| [`equality_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule) | We generate the constraint: input = output |
| [`expand_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.expand_inference_rule) | We generate the exact constraints as we do for tensor additions but we constraint the rank of this expression to be equal to len(n.args[1:]) so that only those cases get considered for the output |
| [`flatten_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.flatten_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.flatten_inference_rule) | |
| [`full_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.full_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.full_inference_rule) | |
| [`gen_broadcasting_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_broadcasting_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_broadcasting_constraints) | |
| [`gen_embedding_rules`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_embedding_rules.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_embedding_rules) | |
| [`gen_layer_norm_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_layer_norm_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.gen_layer_norm_constraints) | |
| [`generate_flatten_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.generate_flatten_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.generate_flatten_constraints) | |
| [`get_attr_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule) | If the attribute is "device" then the tensor shape is preserved |
| [`getitem_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.getitem_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.getitem_inference_rule) | |
| [`gt_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.gt_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.gt_inference_rule) | |
| [`index_select_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule) | We constrain the second argument to a vector or Dyn. |
| [`layer_norm_functional`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_functional.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_functional) | We generate the constraint: input = output |
| [`layer_norm_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule) | Input and output shapes should be equal. |
| [`linear_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_constraints) | |
| [`linear_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule) | Input and output sizes should be the same except for the last dimension If the input is Dyn, then so should the output |
| [`lt_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.lt_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.lt_inference_rule) | |
| [`masked_fill_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule) | Similar to addition. |
| [`maxpool_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.maxpool_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.maxpool_inference_rule) | |
| [`neq_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule) | Translates to inconsistent in gradual types. |
| [`range_check`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.range_check.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.range_check) | Checks if an index i is within range of a size n list :param i: index :param n: list size |
| [`register_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.register_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.register_inference_rule) | |
| [`relu_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.relu_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.relu_inference_rule) | Input and output shapes should be equal. |
| [`reshape_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.reshape_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.reshape_inference_rule) | |
| [`size_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule) | The constraint is just lhs = rhs. |
| [`tensor_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.tensor_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.tensor_inference_rule) | If the tensor is a scalar, we will skip it since we do not support scalars yet. |
| [`torch_dim_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.torch_dim_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.torch_dim_inference_rule) | |
| [`torch_linear_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.torch_linear_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.torch_linear_inference_rule) | |
| [`transpose_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule) | Can be considered as a sequence of two index selects, so we generate constraints accordingly |
| [`type_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.type_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.type_inference_rule) | We generate the constraint: input = output |
| [`view_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule) | Similar to reshape but with an extra condition on the strides |
| [`register_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.register_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.register_inference_rule) | |
| [`transpose_inference_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule) | Can be considered as a sequence of two index selects, so we generate constraints accordingly |
| [`range_check`](generated/torch.fx.experimental.migrate_gradual_types.constraint_generator.range_check.html#torch.fx.experimental.migrate_gradual_types.constraint_generator.range_check) | Checks if an index i is within range of a size n list :param i: index :param n: list size |

## torch.fx.experimental.migrate_gradual_types.constraint_transformation

| [`apply_padding`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.apply_padding.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.apply_padding) | We are considering the possibility where one input has less dimensions than another input, so we apply padding to the broadcasted results |
| --- | --- |
| [`broadcast_dim`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.broadcast_dim.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.broadcast_dim) | Apply broadcasting to the 'index' dimension of tensor_input1. |
| [`calc_last_two_dims`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.calc_last_two_dims.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.calc_last_two_dims) | Generates constraints for the last two dimensions of a convolution or a maxpool output :param constraint: CalcConv or CalcMaxPool :param d: The list of output dimensions |
| [`create_equality_constraints_for_broadcasting`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.create_equality_constraints_for_broadcasting.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.create_equality_constraints_for_broadcasting) | Create equality constraints for when no broadcasting occurs :param e1: Input 1 :param e2: Input 2 :param e11: Broadcasted input 1 :param e12: Broadcasted input 2 :param d1: Variables that store dimensions for e1 :param d2: Variables that store dimensions for e2 :param d11: Variables that store dimensions for e11 :param d12: Variables that store dimensions for e22 |
| [`gen_all_reshape_possibilities`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_all_reshape_possibilities.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_all_reshape_possibilities) | Consider all possibilities what the input dimensions could be (number or dynamic) Then generate the appropriate constraints using multiplication or mod depending on the possibility The possibilities we consider here are the cross product of being equal to dyn or not equal to dyn for the input. |
| [`gen_broadcasting_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_broadcasting_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_broadcasting_constraints) | Simulates broadcasting on e1 and e2 and returns the results respectively in e11 and e12. |
| [`gen_consistency_constraints`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints) | param constraint: Consistency constraint on tensors |
| [`gen_greatest_upper_bound`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound) | param constraint: Greatest upper bound on tensors |
| [`gen_lists_of_dims`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims) | Generate lists of DVar to represent tensor dimensions :param num_tensors: the required number of tensors :param dim_size: the number of dimensions for each tensor :param counter: variable tracking |
| [`generate_all_broadcasting_possibilities_no_padding`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_broadcasting_possibilities_no_padding.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_broadcasting_possibilities_no_padding) | Generate broadcasting constraints assuming no padding. |
| [`generate_all_int_dyn_dim_possibilities`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_int_dyn_dim_possibilities) | Generate all possibilities of being equal or not equal to dyn for my_list :param my_list: List of tensor dimensions |
| [`generate_binconstraint_d`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_binconstraint_d.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_binconstraint_d) | Transform binary constraints for dimensions |
| [`generate_binconstraint_t`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_binconstraint_t.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_binconstraint_t) | Transform binary constraints for tensors |
| [`generate_broadcasting`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_broadcasting.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_broadcasting) | Transform broadcasting constraints |
| [`generate_calc_conv`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_conv.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_conv) | |
| [`generate_calc_maxpool`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_maxpool.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_maxpool) | Transform maxpool constraints |
| [`generate_calc_product`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_product.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_calc_product) | Transform flatten constraints |
| [`generate_conj`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_conj.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_conj) | Transform conjunctions |
| [`generate_d_gub`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_d_gub.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_d_gub) | Transform greatest upper bound for dimensions into equality constraints |
| [`generate_disj`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_disj.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_disj) | Transform disjunctions |
| [`generate_gub`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_gub.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_gub) | Transform greatest upper bound for tensors. |
| [`generate_reshape`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_reshape.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_reshape) | Transform reshape constraints |
| [`is_target_div_by_dim`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim) | Generate constraints to check if the target dimensions are divisible by the input dimensions :param target: Target dimensions :param dim: Input dimensions |
| [`no_broadcast_dim_with_index`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.no_broadcast_dim_with_index.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.no_broadcast_dim_with_index) | param d1: input 1 |
| [`register_transformation_rule`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.register_transformation_rule.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.register_transformation_rule) | |
| [`transform_constraint`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint) | Transforms a constraint into a simpler constraint. |
| [`transform_get_item`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item) | generate an equality of the form: t = [a1, ..., an] then generate constraints that check if the given index is valid given this particular tensor size. |
| [`transform_get_item_tensor`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item_tensor.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item_tensor) | When the index is a tuple, then the output will be a tensor TODO: we have to check if this is the case for all HF models |
| [`transform_index_select`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select) | The constraints consider the given tensor size, checks if the index is valid and if so, generates a constraint for replacing the input dimension with the required dimension |
| [`transform_transpose`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_transpose.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_transpose) | Similar to a sequence of two index-selects |
| [`valid_index`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index) | Given a list of dimensions, checks if an index is valid in the list |
| [`valid_index_tensor`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor) | if the slice instances exceed the length of the dimensions then this is a type error so we return False |
| [`is_dim_div_by_target`](generated/torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target.html#torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target) | Generate constraints to check if the input dimensions is divisible by the target dimensions :param target: Target dimensions :param dim: Input dimensions |

## torch.fx.experimental.graph_gradual_typechecker

| [`adaptiveavgpool2d_check`](generated/torch.fx.experimental.graph_gradual_typechecker.adaptiveavgpool2d_check.html#torch.fx.experimental.graph_gradual_typechecker.adaptiveavgpool2d_check) | |
| --- | --- |
| [`adaptiveavgpool2d_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.adaptiveavgpool2d_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.adaptiveavgpool2d_inference_rule) | The input and output sizes should be the same except for the last two dimensions taken from the input, which represent width and height |
| [`add_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.add_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.add_inference_rule) | Apply the addition inference rule. |
| [`all_eq`](generated/torch.fx.experimental.graph_gradual_typechecker.all_eq.html#torch.fx.experimental.graph_gradual_typechecker.all_eq) | For operations where the input shape is equal to the output shape |
| [`bn2d_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.bn2d_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.bn2d_inference_rule) | Given a BatchNorm2D instance and a node check the following conditions: - the input type can be expanded to a size 4 tensor: t = (x_1, x_2, x_3, x_4) - the current node type can be expanded to a size 4 tensor: t' = (x_1', x_2', x_3', x_4') - t is consistent with t' - x_2 is consistent with the module's num_features - x_2' is consistent with the module's num_features output type: the more precise type of t and t' |
| [`broadcast_types`](generated/torch.fx.experimental.graph_gradual_typechecker.broadcast_types.html#torch.fx.experimental.graph_gradual_typechecker.broadcast_types) | Applies broadcasting to both given types such that they become consistent with each other and returns two new resulting types |
| [`calculate_out_dimension`](generated/torch.fx.experimental.graph_gradual_typechecker.calculate_out_dimension.html#torch.fx.experimental.graph_gradual_typechecker.calculate_out_dimension) | For calculating h_in and w_out according to the conv2D documentation |
| [`conv2d_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.conv2d_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.conv2d_inference_rule) | Given a Conv2D instance and a node check the following conditions: - the input type can be expanded to a size 4 tensor: t = (x_1, x_2, H, W) - the current node type can be expanded to a size 4 tensor: t' = (x_1', x_2', x_3', x_4') - x_2 is consistent with the module's in_channels - let o = (x_1, out_channels, H_out, W_out) then the output is the greatest upper bound of o and the existing node type t'. |
| [`conv_refinement_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.conv_refinement_rule.html#torch.fx.experimental.graph_gradual_typechecker.conv_refinement_rule) | The equality constraints are between the first dimension of the input and output |
| [`conv_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.conv_rule.html#torch.fx.experimental.graph_gradual_typechecker.conv_rule) | Represents the output in terms of an algebraic expression w.r.t the input when possible |
| [`element_wise_eq`](generated/torch.fx.experimental.graph_gradual_typechecker.element_wise_eq.html#torch.fx.experimental.graph_gradual_typechecker.element_wise_eq) | For element-wise operations and handles broadcasting. |
| [`expand_to_tensor_dim`](generated/torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim.html#torch.fx.experimental.graph_gradual_typechecker.expand_to_tensor_dim) | Expand a type to the desired tensor dimension if possible Raise an error otherwise. |
| [`first_two_eq`](generated/torch.fx.experimental.graph_gradual_typechecker.first_two_eq.html#torch.fx.experimental.graph_gradual_typechecker.first_two_eq) | For operations where the first two dimensions of the input and output shape are equal |
| [`flatten_check`](generated/torch.fx.experimental.graph_gradual_typechecker.flatten_check.html#torch.fx.experimental.graph_gradual_typechecker.flatten_check) | |
| [`flatten_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.flatten_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.flatten_inference_rule) | Applies the flatten shape information to the input then gets the greatest upper bound of the resulting type and the existing type |
| [`flatten_refinement_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.flatten_refinement_rule.html#torch.fx.experimental.graph_gradual_typechecker.flatten_refinement_rule) | Generates equality constraints between the dimensions of the input and output that will not be involved in the flatten operation |
| [`get_attr_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.get_attr_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.get_attr_inference_rule) | The current getattr rule only handles the shape attribute Can be extended to other attributes The most representative type we have is "Dyn" but the system can be extended with more types, such as a type to represent shapes |
| [`get_greatest_upper_bound`](generated/torch.fx.experimental.graph_gradual_typechecker.get_greatest_upper_bound.html#torch.fx.experimental.graph_gradual_typechecker.get_greatest_upper_bound) | Get the most precise type that's consistent with the given types |
| [`get_parameter`](generated/torch.fx.experimental.graph_gradual_typechecker.get_parameter.html#torch.fx.experimental.graph_gradual_typechecker.get_parameter) | Returns the parameter given by `target` if it exists, otherwise throws an error. |
| [`GraphTypeChecker`](generated/torch.fx.experimental.graph_gradual_typechecker.GraphTypeChecker.html#torch.fx.experimental.graph_gradual_typechecker.GraphTypeChecker) | |
| [`linear_check`](generated/torch.fx.experimental.graph_gradual_typechecker.linear_check.html#torch.fx.experimental.graph_gradual_typechecker.linear_check) | Checks that an input tensor type satisfies the conditions for linear operation and returns the output type based on in and out features given by module_instance |
| [`linear_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.linear_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.linear_inference_rule) | Applies the shape information to the input then gets the greatest upper bound of the resulting type and the existing type |
| [`linear_refinement_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.linear_refinement_rule.html#torch.fx.experimental.graph_gradual_typechecker.linear_refinement_rule) | The equality constraints are between the first dimension of the input and output |
| [`maxpool2d_check`](generated/torch.fx.experimental.graph_gradual_typechecker.maxpool2d_check.html#torch.fx.experimental.graph_gradual_typechecker.maxpool2d_check) | Applies the maxpool2d shape information to the input this affects the last two dimensions |
| [`maxpool2d_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.maxpool2d_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.maxpool2d_inference_rule) | Given a MaxPool2D instance and a node check the following conditions: |
| [`register_algebraic_expressions_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.register_algebraic_expressions_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.register_algebraic_expressions_inference_rule) | |
| [`register_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.register_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.register_inference_rule) | |
| [`register_refinement_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.register_refinement_rule.html#torch.fx.experimental.graph_gradual_typechecker.register_refinement_rule) | |
| [`relu_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.relu_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.relu_inference_rule) | Input and output shapes should be equal. |
| [`reshape_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.reshape_inference_rule) | Without dynamism, the rule checks that the product of the elements of the argument tensor type is equal to the product of the elements of the required shape. |
| [`transpose_inference_rule`](generated/torch.fx.experimental.graph_gradual_typechecker.transpose_inference_rule.html#torch.fx.experimental.graph_gradual_typechecker.transpose_inference_rule) | We check that dimensions for the transpose operations are within range of the tensor type of the node |

## torch.fx.experimental.meta_tracer

| [`embedding_override`](generated/torch.fx.experimental.meta_tracer.embedding_override.html#torch.fx.experimental.meta_tracer.embedding_override) | |
| --- | --- |
| [`functional_relu_override`](generated/torch.fx.experimental.meta_tracer.functional_relu_override.html#torch.fx.experimental.meta_tracer.functional_relu_override) | |
| [`gen_constructor_wrapper`](generated/torch.fx.experimental.meta_tracer.gen_constructor_wrapper.html#torch.fx.experimental.meta_tracer.gen_constructor_wrapper) | |
| [`nn_layernorm_override`](generated/torch.fx.experimental.meta_tracer.nn_layernorm_override.html#torch.fx.experimental.meta_tracer.nn_layernorm_override) | |
| [`proxys_to_metas`](generated/torch.fx.experimental.meta_tracer.proxys_to_metas.html#torch.fx.experimental.meta_tracer.proxys_to_metas) | |
| [`symbolic_trace`](generated/torch.fx.experimental.meta_tracer.symbolic_trace.html#torch.fx.experimental.meta_tracer.symbolic_trace) | |
| [`torch_abs_override`](generated/torch.fx.experimental.meta_tracer.torch_abs_override.html#torch.fx.experimental.meta_tracer.torch_abs_override) | |
| [`torch_nn_relu_override`](generated/torch.fx.experimental.meta_tracer.torch_nn_relu_override.html#torch.fx.experimental.meta_tracer.torch_nn_relu_override) | |
| [`torch_relu_override`](generated/torch.fx.experimental.meta_tracer.torch_relu_override.html#torch.fx.experimental.meta_tracer.torch_relu_override) | |
| [`torch_where_override`](generated/torch.fx.experimental.meta_tracer.torch_where_override.html#torch.fx.experimental.meta_tracer.torch_where_override) | |

## torch.fx.experimental.accelerator_partitioner

| [`check_dependency`](generated/torch.fx.experimental.accelerator_partitioner.check_dependency.html#torch.fx.experimental.accelerator_partitioner.check_dependency) | Given a partition,check if there is a circular dependency on this partition using bfs |
| --- | --- |
| [`combine_two_partitions`](generated/torch.fx.experimental.accelerator_partitioner.combine_two_partitions.html#torch.fx.experimental.accelerator_partitioner.combine_two_partitions) | Given a list of partitions and its two partitions, combine these two partitions into a new one appending to the partitions and remove the previous two partitions from the list of partitions |
| [`reorganize_partitions`](generated/torch.fx.experimental.accelerator_partitioner.reorganize_partitions.html#torch.fx.experimental.accelerator_partitioner.reorganize_partitions) | Given a list of partitions, reorganize partition id, its parents and its children for each partition |
| [`reset_partition_device`](generated/torch.fx.experimental.accelerator_partitioner.reset_partition_device.html#torch.fx.experimental.accelerator_partitioner.reset_partition_device) | |
| [`set_parents_and_children`](generated/torch.fx.experimental.accelerator_partitioner.set_parents_and_children.html#torch.fx.experimental.accelerator_partitioner.set_parents_and_children) | Given a list of partitions, mark parents and children for each partition |

## torch.fx.experimental.debug

| [`set_trace`](generated/torch.fx.experimental.debug.set_trace.html#torch.fx.experimental.debug.set_trace) | Sets a breakpoint in gm's generated python code. |
| --- | --- |

## torch.fx.experimental.merge_matmul

| [`are_nodes_independent`](generated/torch.fx.experimental.merge_matmul.are_nodes_independent.html#torch.fx.experimental.merge_matmul.are_nodes_independent) | Check if all of the given nodes are pairwise-data independent. |
| --- | --- |
| [`may_depend_on`](generated/torch.fx.experimental.merge_matmul.may_depend_on.html#torch.fx.experimental.merge_matmul.may_depend_on) | Determine if one node depends on another in a torch.fx.Graph. |
| [`merge_matmul`](generated/torch.fx.experimental.merge_matmul.merge_matmul.html#torch.fx.experimental.merge_matmul.merge_matmul) | A graph transformation that merges matrix multiplication operations that share the same right-hand side operand into one large matrix multiplication. |

## torch.fx.experimental.unification.match

| [`edge`](generated/torch.fx.experimental.unification.match.edge.html#torch.fx.experimental.unification.match.edge) | A should be checked before B Tie broken by tie_breaker, defaults to `hash` |
| --- | --- |
| [`match`](generated/torch.fx.experimental.unification.match.match.html#torch.fx.experimental.unification.match.match) | |
| [`ordering`](generated/torch.fx.experimental.unification.match.ordering.html#torch.fx.experimental.unification.match.ordering) | A sane ordering of signatures to check, first to last Topological sort of edges as given by `edge` and `supercedes` |
| [`supercedes`](generated/torch.fx.experimental.unification.match.supercedes.html#torch.fx.experimental.unification.match.supercedes) | `a` is a more specific match than `b` |

## torch.fx.experimental.unification.more

| [`reify_object`](generated/torch.fx.experimental.unification.more.reify_object.html#torch.fx.experimental.unification.more.reify_object) | Reify a Python object with a substitution >>> class Foo(object): . |
| --- | --- |
| [`unifiable`](generated/torch.fx.experimental.unification.more.unifiable.html#torch.fx.experimental.unification.more.unifiable) | Register standard unify and reify operations on class This uses the type and __dict__ or __slots__ attributes to define the nature of the term See Also: >>> class A(object): . |
| [`unify_object`](generated/torch.fx.experimental.unification.more.unify_object.html#torch.fx.experimental.unification.more.unify_object) | Unify two Python objects Unifies their type and `__dict__` attributes >>> class Foo(object): . |

## torch.fx.experimental.unification.multipledispatch.conflict

| [`ambiguities`](generated/torch.fx.experimental.unification.multipledispatch.conflict.ambiguities.html#torch.fx.experimental.unification.multipledispatch.conflict.ambiguities) | All signature pairs such that A is ambiguous with B |
| --- | --- |
| [`ambiguous`](generated/torch.fx.experimental.unification.multipledispatch.conflict.ambiguous.html#torch.fx.experimental.unification.multipledispatch.conflict.ambiguous) | A is consistent with B but neither is strictly more specific |
| [`consistent`](generated/torch.fx.experimental.unification.multipledispatch.conflict.consistent.html#torch.fx.experimental.unification.multipledispatch.conflict.consistent) | It is possible for an argument list to satisfy both A and B |
| [`edge`](generated/torch.fx.experimental.unification.multipledispatch.conflict.edge.html#torch.fx.experimental.unification.multipledispatch.conflict.edge) | A should be checked before B Tie broken by tie_breaker, defaults to `hash` |
| [`ordering`](generated/torch.fx.experimental.unification.multipledispatch.conflict.ordering.html#torch.fx.experimental.unification.multipledispatch.conflict.ordering) | A sane ordering of signatures to check, first to last Topological sort of edges as given by `edge` and `supercedes` |
| [`super_signature`](generated/torch.fx.experimental.unification.multipledispatch.conflict.super_signature.html#torch.fx.experimental.unification.multipledispatch.conflict.super_signature) | A signature that would break ambiguities |
| [`supercedes`](generated/torch.fx.experimental.unification.multipledispatch.conflict.supercedes.html#torch.fx.experimental.unification.multipledispatch.conflict.supercedes) | A is consistent and strictly more specific than B |

## torch.fx.experimental.unification.multipledispatch.core

| [`dispatch`](generated/torch.fx.experimental.unification.multipledispatch.core.dispatch.html#torch.fx.experimental.unification.multipledispatch.core.dispatch) | Dispatch function on the types of the inputs Supports dispatch on all non-keyword arguments. |
| --- | --- |
| [`ismethod`](generated/torch.fx.experimental.unification.multipledispatch.core.ismethod.html#torch.fx.experimental.unification.multipledispatch.core.ismethod) | Is func a method? Note that this has to work as the method is defined but before the class is defined. |

## torch.fx.experimental.unification.multipledispatch.dispatcher

| [`ambiguity_warn`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn.html#torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn) | Raise warning when ambiguity is detected. |
| --- | --- |
| [`halt_ordering`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.halt_ordering.html#torch.fx.experimental.unification.multipledispatch.dispatcher.halt_ordering) | Deprecated interface to temporarily disable ordering. |
| [`restart_ordering`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.restart_ordering.html#torch.fx.experimental.unification.multipledispatch.dispatcher.restart_ordering) | Deprecated interface to temporarily resume ordering. |
| [`source`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.source.html#torch.fx.experimental.unification.multipledispatch.dispatcher.source) | |
| [`str_signature`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.str_signature.html#torch.fx.experimental.unification.multipledispatch.dispatcher.str_signature) | String representation of type signature >>> str_signature((int, float)) 'int, float' |
| [`variadic_signature_matches`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches.html#torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches) | |
| [`variadic_signature_matches_iter`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches_iter.html#torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches_iter) | Check if a set of input types matches a variadic signature. |
| [`warning_text`](generated/torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text.html#torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text) | The text for ambiguity warnings |

## torch.fx.experimental.unification.multipledispatch.variadic

| [`isvariadic`](generated/torch.fx.experimental.unification.multipledispatch.variadic.isvariadic.html#torch.fx.experimental.unification.multipledispatch.variadic.isvariadic) | Check whether the type obj is variadic. |
| --- | --- |

## torch.fx.experimental.unification.utils

| [`freeze`](generated/torch.fx.experimental.unification.utils.freeze.html#torch.fx.experimental.unification.utils.freeze) | Freeze container to hashable form >>> freeze(1) 1 >>> freeze([1, 2]) (1, 2) >>> freeze({1: 2}) # doctest: +SKIP frozenset([(1, 2)]) |
| --- | --- |
| [`hashable`](generated/torch.fx.experimental.unification.utils.hashable.html#torch.fx.experimental.unification.utils.hashable) | |
| [`raises`](generated/torch.fx.experimental.unification.utils.raises.html#torch.fx.experimental.unification.utils.raises) | |
| [`reverse_dict`](generated/torch.fx.experimental.unification.utils.reverse_dict.html#torch.fx.experimental.unification.utils.reverse_dict) | Reverses direction of dependence dict. |
| [`transitive_get`](generated/torch.fx.experimental.unification.utils.transitive_get.html#torch.fx.experimental.unification.utils.transitive_get) | Transitive dict.get >>> d = {1: 2, 2: 3, 3: 4} >>> d.get(1) 2 >>> transitive_get(1, d) 4 |
| [`xfail`](generated/torch.fx.experimental.unification.utils.xfail.html#torch.fx.experimental.unification.utils.xfail) | |

## torch.fx.experimental.unification.variable

| [`var`](generated/torch.fx.experimental.unification.variable.var.html#torch.fx.experimental.unification.variable.var) | |
| --- | --- |
| [`variables`](generated/torch.fx.experimental.unification.variable.variables.html#torch.fx.experimental.unification.variable.variables) | Context manager for logic variables |
| [`vars`](generated/torch.fx.experimental.unification.variable.vars.html#torch.fx.experimental.unification.variable.vars) | |

## torch.fx.experimental.unify_refinements

| [`check_for_type_equality`](generated/torch.fx.experimental.unify_refinements.check_for_type_equality.html#torch.fx.experimental.unify_refinements.check_for_type_equality) | A check equality to be used in fixed points. |
| --- | --- |
| [`convert_eq`](generated/torch.fx.experimental.unify_refinements.convert_eq.html#torch.fx.experimental.unify_refinements.convert_eq) | Convert equality constraints in the right format to be used by unification library. |
| [`infer_symbolic_types`](generated/torch.fx.experimental.unify_refinements.infer_symbolic_types.html#torch.fx.experimental.unify_refinements.infer_symbolic_types) | Calls our symbolic inferencer twice. |
| [`infer_symbolic_types_single_pass`](generated/torch.fx.experimental.unify_refinements.infer_symbolic_types_single_pass.html#torch.fx.experimental.unify_refinements.infer_symbolic_types_single_pass) | Calls our symbolic inferencer once. |
| [`substitute_all_types`](generated/torch.fx.experimental.unify_refinements.substitute_all_types.html#torch.fx.experimental.unify_refinements.substitute_all_types) | Apply the most general unifier to all types in a graph till reaching a fixed point. |
| [`substitute_solution_one_type`](generated/torch.fx.experimental.unify_refinements.substitute_solution_one_type.html#torch.fx.experimental.unify_refinements.substitute_solution_one_type) | Apply the most general unifier to a type |
| [`unify_eq`](generated/torch.fx.experimental.unify_refinements.unify_eq.html#torch.fx.experimental.unify_refinements.unify_eq) | Apply unification to a set of equality constraints |

## torch.fx.experimental.validator

| [`bisect`](generated/torch.fx.experimental.validator.bisect.html#torch.fx.experimental.validator.bisect) | |
| --- | --- |
| [`TranslationValidator`](generated/torch.fx.experimental.validator.TranslationValidator.html#torch.fx.experimental.validator.TranslationValidator) | |
| [`translation_validation_enabled`](generated/torch.fx.experimental.validator.translation_validation_enabled.html#torch.fx.experimental.validator.translation_validation_enabled) | |
| [`translation_validation_timeout`](generated/torch.fx.experimental.validator.translation_validation_timeout.html#torch.fx.experimental.validator.translation_validation_timeout) | |
| [`z3op`](generated/torch.fx.experimental.validator.z3op.html#torch.fx.experimental.validator.z3op) | |
| [`z3str`](generated/torch.fx.experimental.validator.z3str.html#torch.fx.experimental.validator.z3str) | |