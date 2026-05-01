# Joint with descriptors

Joint with descriptors is an experimental API for exporting a traced joint
graph that supports all of torch.compile's features in full generality and,
after processing, can be converted back into a differentiable callable that
can be executed as normal. For example, it is used to implement autoparallel,
a system that takes a model and reshards inputs and parameters to make it
a distributed SPMD program.

torch._functorch.aot_autograd.aot_export_joint_with_descriptors(*stack*, *mod*, *args*, *kwargs=None*, ***, *decompositions=None*, *keep_inference_input_mutations=False*, *ignore_shape_env=False*, *disable_functionalization=False*, *_record_nn_module_stack=False*, *_disable_torch_fn_metadata_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/aot_autograd.py#L1304)

This API captures the joint graph for an nn.Module. However, unlike
aot_export_joint_simple or aot_export_module(trace_joint=True), the
calling convention of the produced joint graph follows no fixed positional
schema; for example, you cannot rely on the second argument of the traced
joint graph to correspond to the second argument of the module you traced.
However, the inputs and outputs of the traced graph are schematized
with **descriptors**, annotated on meta['desc'] on the placeholder and
return FX nodes, which you can use to determine the meaning of arguments.

The major benefit of using this export rather than aot_export_joint_simple
is that we have feature parity with all situations that torch.compile
supports (via aot_module_simplified), including handling for more
complicated cases such as multiple differentiable outputs, input mutations
that must be handled outside of the graph, tensor subclasses, etc.

What can you do with one of these joint graphs with descriptors? The
motivating use case (autoparallel) involves taking the joint graph, doing
optimizations on it, and then turning it back into a callable so it can be
torch.compile'd at a later point in time. This cannot be done as a
traditional torch.compile joint graph pass for two reasons:

> 1. The sharding of parameters must be decided before parameter
> initialization / checkpoint load, far before torch.compile would
> ordinarily run.
> 2. We need to change the meaning of parameters (e.g., we might replace
> a replicated parameter with a sharded version of it, changing its
> input size). torch.compile is ordinarily semantics preserving, and
> not allowed to change the meaning of inputs.

Some descriptors can be quite exotic, so we recommend thinking carefully
if there is a safe fallback you can apply to descriptors you don't understand.
For example, you should have some way to handle not finding a particular
input exactly as is in the final FX graph inputs.

Note: When using this API, you must create and enter an ExitStack context
manager, which will be passed into this function. This context manager
must remain active if you call the compile function to finish compilation.
(TODO: We may relax this requirement by having AOTAutograd keep track of
how to reconstruct all the context managers at a later point in time.)

NB: You're not obligated to do a /full/ compile in stage2; instead you can
leave the forward/backward compilers unspecified in which case the
partitioned FX graphs will directly run. The overall autograd Function
can be allowed in graph so you can reprocess it in the context of a
(potentially larger) compiled region later.

NB: These APIs do NOT hit cache, as we only ever cache the final compile results,
not the intermediate export result.

NB: If the passed nn.Module has parameters and buffers on it, we will
generate extra implicit parameter/buffer arguments and assign ParamAOTInput
and BufferAOTInput descriptors to them. However, if you generate the input
nn.Module from a mechanism like Dynamo, you will NOT get these descriptors
(because Dynamo will already have taken care of lifting the parameters/buffers
into arguments!) In that case, it would be necessary to analyze the Sources
of the inputs to determine if inputs are parameters and their FQNs.

Return type:

JointWithDescriptors

torch._functorch.aot_autograd.aot_compile_joint_with_descriptors(*jd*, ***, *partition_fn=<function default_partition>*, *fw_compiler=<function boxed_nop_preserve_node_meta>*, *bw_compiler=<function boxed_nop_preserve_node_meta>*, *serializable=False*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/aot_autograd.py#L1442)

Companion function for aot_export_joint_with_descriptors which compiles the joint
graph into a callable function that follows a standard calling convention.
params_flat all are arguments.

Note: We do NOT instantiate the module; this gives you the flexibility to subclass it and
customize its behavior without having to worry about FQN rebinding.

Parameters:

**serializable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, configures the compilation to produce a serializable
callable by leveraging AOTAutogradCache machinery. This sets up the
necessary cache_info and patches config options required for serialization.
When True, this function will always return a BundledAOTAutogradSerializableCallable.

Return type:

Callable[..., Any]

## Descriptors

*class*torch._functorch._aot_autograd.descriptors.AOTInput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L327)

Describes where an input from an AOTAutograd produced FX graph comes from

is_buffer()[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L338)

True if this input is a buffer or derived from a buffer (e.g., subclass attr)

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

is_param()[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L334)

True if this input is a parameter or derived from a parameter (e.g., subclass attr)

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

is_tangent()[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L342)

True if this input is a tangent or derived from a tangent (e.g., subclass attr)

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch._functorch._aot_autograd.descriptors.AOTOutput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L356)

Describes where an output from an AOTAutograd produced FX graph will
eventually be bundled into the final output

is_grad()[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L364)

True if this output is a grad or derived from a grad (e.g., subclass attr)

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch._functorch._aot_autograd.descriptors.BackwardTokenAOTInput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L559)

The world token which is threaded through side-effectful operations, for backwards

*class*torch._functorch._aot_autograd.descriptors.BackwardTokenAOTOutput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L689)

The world token output for side-effectful calls, returned so we cannot DCE it, backward only

*class*torch._functorch._aot_autograd.descriptors.BufferAOTInput(*target*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L397)

The input is a buffer, whose FQN is target

*class*torch._functorch._aot_autograd.descriptors.DummyAOTInput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L413)

In some circumstances, we want to call into a function that expects AOTInput, but
we don't actually care about that logic (most typically, because some code is being used
for both compile-time and run-time; AOTInput processing is not needed in this situation.
Pass a dummy in this situation; but it is better to just have a version of the function
that doesn't have this at all.

*class*torch._functorch._aot_autograd.descriptors.DummyAOTOutput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L739)

For cases when you don't actually care about descriptor propagation, do not use under normal
circumstances.

*class*torch._functorch._aot_autograd.descriptors.GradAOTOutput(*grad_of*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L644)

An output representing the computed gradient for a differentiable input, in the joint graph

*class*torch._functorch._aot_autograd.descriptors.InputMutationAOTOutput(*mutated_input*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L610)

The mutated value of an input tensor, returned so we can appropriately propagate autograd.

*class*torch._functorch._aot_autograd.descriptors.IntermediateBaseAOTOutput(*base_of*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L620)

An intermediate base of multiple outputs which alias each other. We only report ONE of
the outputs that contributed to this base

*class*torch._functorch._aot_autograd.descriptors.ParamAOTInput(*target*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L381)

The input is a parameter, whose FQN is target

*class*torch._functorch._aot_autograd.descriptors.PhiloxBackwardBaseOffsetAOTInput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L541)

The offset for functionalized Philox RNG calls, specifically for backward graph.

*class*torch._functorch._aot_autograd.descriptors.PhiloxBackwardSeedAOTInput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L533)

The seed for functionalized Philox RNG calls, specifically for backward graph.

*class*torch._functorch._aot_autograd.descriptors.PhiloxForwardBaseOffsetAOTInput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L525)

The offset for functionalized Philox RNG calls, specifically for forward graph.

*class*torch._functorch._aot_autograd.descriptors.PhiloxForwardSeedAOTInput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L517)

The seed for functionalized Philox RNG calls, specifically for forward graph.

*class*torch._functorch._aot_autograd.descriptors.PhiloxUpdatedBackwardOffsetAOTOutput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L671)

The final offset from the functionalized RNG calls, backward only

*class*torch._functorch._aot_autograd.descriptors.PhiloxUpdatedForwardOffsetAOTOutput[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L663)

The final offset from the functionalized RNG calls, forward only

*class*torch._functorch._aot_autograd.descriptors.PlainAOTInput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L427)

The input is a plain input, corresponding to a particular positional index.

Note that AOTInput is always relative to a function with a *flat* calling convention,
e.g., as accepted by aot_module_simplified. There are some AOTAutograd APIs that
flatten pytrees, and we don't record PyTree key paths from the flattening (but we
could and should!)

*class*torch._functorch._aot_autograd.descriptors.PlainAOTOutput(*idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L600)

A plain tensor output at position idx of the output tuple

*class*torch._functorch._aot_autograd.descriptors.SavedForBackwardsAOTOutput(*idx: [int](https://docs.python.org/3/library/functions.html#int)*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L750)

*class*torch._functorch._aot_autograd.descriptors.SubclassGetAttrAOTInput(*base*, *attr*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L443)

Subclass inputs get unpacked into their constituent pieces before going into an FX
graph. This tells you which particular attribute of the subclass this particular
input corresponds to (of the 'base' originally subclass argument.)

*class*torch._functorch._aot_autograd.descriptors.SubclassGetAttrAOTOutput(*base*, *attr*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L703)

This output will be bundled into a subclass at this location

*class*torch._functorch._aot_autograd.descriptors.SubclassSizeAOTInput(*base*, *idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L466)

Which subclass this particular outer size SymInt input (at dim idx) came from.

*class*torch._functorch._aot_autograd.descriptors.SubclassSizeAOTOutput(*base*, *idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L717)

This output size will be bundled into a subclass at this location

*class*torch._functorch._aot_autograd.descriptors.SubclassStrideAOTInput(*base*, *idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L477)

Which subclass this particular outer stride SymInt input (at dim idx) came from.

*class*torch._functorch._aot_autograd.descriptors.SubclassStrideAOTOutput(*base*, *idx*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L728)

This output stride will be bundled into a subclass at this location

*class*torch._functorch._aot_autograd.descriptors.SyntheticBaseAOTInput(*base_of*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L504)

This is similar to ViewBaseAOTInput, but this happens when none of the views were differentiable, so
we weren't able to get our hands on the true original view and constructed a synthetic one instead
for the sake of autograd.

*class*torch._functorch._aot_autograd.descriptors.ViewBaseAOTInput(*base_of*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/descriptors.py#L488)

When multiple differentiable inputs are views of the same input, AOTAutograd will replace all of these
views with a single input representing the base. If this is undesirable, you can clone the views
example inputs before passing them into AOTAutograd.

TODO: In principle we could report ALL of the inputs who this is a base of.

## FX utilities

This module contains utility functions for working with joint FX graphs with descriptors
that are produced by AOTAutograd. They will NOT work on generic FX graphs. See also
`torch._functorch.aot_autograd.aot_export_joint_with_descriptors()`. We also
recommend reading :mod:torch._functorch._aot_autograd.descriptors`.

torch._functorch._aot_autograd.fx_utils.get_all_input_and_grad_nodes(*g*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L44)

Given a joint graph with descriptors (meta['desc'] on placeholders and
output), returns the node for every input and its corresponding grad
output node if it exists. These tuples are in a dict that is indexed by
the AOTInput descriptor that describes the input.

NB: *all* forward tensor inputs are returned, including non-differentiable
inputs (which simply have a None grad), so it is safe to use this function
to perform operations on all inputs. (Non-tensor inputs like symbolic
integers, tokens or RNG state are NOT traversed by this function.)

Parameters:

**g** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A dictionary mapping each DifferentiableAOTInput descriptor to a tuple
containing:
- The input node itself
- The grad (output) node if it exists, None otherwise

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If the joint graph has subclass tensor inputs/outputs; this
- **is not supported by API as there is not necessarily a 1-1 correspondence** -
- **between inputs and grads when subclasses are involved.** -

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*DifferentiableAOTInput*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Node*](../../../fx.html#torch.fx.Node), [*Node*](../../../fx.html#torch.fx.Node) | None]]

torch._functorch._aot_autograd.fx_utils.get_all_output_and_tangent_nodes(*g*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L100)

Get all output nodes and their corresponding tangent nodes from a joint graph.

Similar to get_all_input_and_grad_nodes, but returns output nodes paired with
their tangent nodes (if they exist). This function traverses the graph to find
all differentiable outputs and matches them with their corresponding tangent
inputs used in forward-mode autodiff.

NB: *all* forward tensor output sare turned, including non-differentiable outputs,
so you can use this function to perform operations on all outputs.

Parameters:

**g** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A dictionary mapping each DifferentiableAOTOutput descriptor to a tuple
containing:
- The output node itself
- The tangent (input) node if it exists, None otherwise

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If the joint graph has subclass tensor inputs/outputs; this
- **is not supported by API as there is not necessarily a 1-1 correspondence** -
- **between outputs and tangents when subclasses are involved.** -

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*DifferentiableAOTOutput*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Node*](../../../fx.html#torch.fx.Node), [*Node*](../../../fx.html#torch.fx.Node) | None]]

torch._functorch._aot_autograd.fx_utils.get_buffer_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L307)

Get all buffer nodes from a graph as a list.

You can rely on this providing the correct order of buffers you need
to feed into the joint graph (after parameters).

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A list of FX nodes representing all buffers in the graph.

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If subclass tensors are encountered (not yet supported), as
- **it is not clear if you wanted each individual constituent piece****of****the** -
- **subclasses****, or****have them grouped up in some way.** -

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Node*](../../../fx.html#torch.fx.Node)]

torch._functorch._aot_autograd.fx_utils.get_named_buffer_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L258)

Get buffer nodes mapped by their fully qualified names.

This function traverses the graph to find all buffer input nodes and
returns them in a dictionary where keys are the buffer names (FQNs)
and values are the corresponding FX nodes.

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A dictionary mapping buffer names (str) to their corresponding FX nodes.

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If subclass tensors are encountered (not yet supported), as
- **with subclasses a FQN does not necessarily map to a single plain tensor.** -

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Node*](../../../fx.html#torch.fx.Node)]

torch._functorch._aot_autograd.fx_utils.get_named_param_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L230)

Get parameter nodes mapped by their fully qualified names.

This function traverses the graph to find all parameter input nodes and
returns them in a dictionary where keys are the parameter names (FQNs)
and values are the corresponding FX nodes.

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A dictionary mapping parameter names (str) to their corresponding FX nodes.

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If subclass tensors are encountered (not yet supported), as
- **with subclasses a FQN does not necessarily map to a single plain tensor.** -

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Node*](../../../fx.html#torch.fx.Node)]

torch._functorch._aot_autograd.fx_utils.get_param_and_grad_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L154)

Get parameter nodes and their corresponding gradient nodes from a joint graph.

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

- The parameter input node
- The gradient (output) node if it exists, None otherwise

Return type:

A dictionary mapping each ParamAOTInput descriptor to a tuple containing

torch._functorch._aot_autograd.fx_utils.get_param_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L286)

Get all parameter nodes from a graph as a list.

You can rely on this providing the correct order of parameters you need
to feed into the joint graph (at the very beginning of the argument list,
before buffers).

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

A list of FX nodes representing all parameters in the graph.

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If subclass tensors are encountered (not yet supported), as
- **it is not clear if you wanted each individual constituent piece****of****the** -
- **subclasses****, or****have them grouped up in some way.** -

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Node*](../../../fx.html#torch.fx.Node)]

torch._functorch._aot_autograd.fx_utils.get_plain_input_and_grad_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L174)

Get plain input nodes and their corresponding gradient nodes from a joint graph.

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

- The plain input node
- The gradient (output) node if it exists, None otherwise

Return type:

A dictionary mapping each PlainAOTInput descriptor to a tuple containing

torch._functorch._aot_autograd.fx_utils.get_plain_output_and_tangent_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/_functorch/_aot_autograd/fx_utils.py#L194)

Get plain output nodes and their corresponding tangent nodes from a joint graph.

Parameters:

**graph** ([*Graph*](../../../fx.html#torch.fx.Graph)) - The FX joint graph with descriptors

Returns:

- The plain output node
- The tangent (input) node if it exists, None otherwise

Return type:

A dictionary mapping each PlainAOTOutput descriptor to a tuple containing