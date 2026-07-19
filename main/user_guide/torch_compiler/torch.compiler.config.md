# torch.compiler.config

This is the top-level configuration module for the compiler, containing
cross-cutting configuration options that affect all parts of the compiler
stack.

You may also be interested in the per-component configuration modules, which
contain configuration options that affect only a specific part of the compiler:

- `torch._dynamo.config`
- `torch._inductor.config`
- `torch._functorch.config`
- `torch.fx.experimental.config`

torch.compiler.config.accumulated_recompile_limit*: [int](https://docs.python.org/3/library/functions.html#int)**= 256*

Global limit on total recompilations across all compiled functions to prevent
runaway recompilation scenarios. This safeguard protects against compilation
performance issues that could affect the entire program.

torch.compiler.config.allow_unspec_int_on_nn_module*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Allows integer attributes of nn.Module instances to be unspecialized through
the dynamic shape mechanism. By default, TorchDynamo specializes on all integer
module attributes, but this can cause excessive recompilation when integers
like step counters change frequently.

torch.compiler.config.assume_static_by_default*: [bool](https://docs.python.org/3/library/functions.html#bool)**= True*

When enabled, all tensor dimensions are assumed to be static unless explicitly
marked as dynamic or detected as changing. This compilation-wide behavior affects
how the entire stack handles shape specialization and can improve performance
for static workloads.

torch.compiler.config.automatic_dynamic_shapes*: [bool](https://docs.python.org/3/library/functions.html#bool)**= True*

Enables automatic detection and handling of dynamic shapes. When a tensor's
shape changes between compilations, the system automatically marks those
dimensions as dynamic rather than requiring manual specification. This
cross-cutting optimization improves the user experience by reducing recompilations.

torch.compiler.config.capture_dynamic_output_shape_ops*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Controls whether TorchDynamo captures operations with dynamic output shapes (like
nonzero, unique) into the FX graph. When disabled, these operations cause graph breaks.
This is a TorchDynamo-specific setting for handling operations with unpredictable
output shapes during tracing.

torch.compiler.config.capture_scalar_outputs*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Controls whether TorchDynamo captures operations that return scalar values (like .item())
into the FX graph. When disabled, these operations cause graph breaks. This is a
TorchDynamo-specific tracing behavior that affects how the tracer handles
scalar-returning operations.

torch.compiler.config.compile_on_one_rank*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

When enabled, device- and rank-specific values (devices, process groups) are computed at
runtime via custom ops rather than baked in at compile time, so a graph can be compiled on
one rank and run on all ranks. Read across the stack: make_fx, inductor, and distributed.

torch.compiler.config.dynamic_shapes*: [bool](https://docs.python.org/3/library/functions.html#bool)**= True*

Controls whether the compilation pipeline supports dynamic tensor shapes.
When enabled, the compiler can handle tensors with varying dimensions across
different invocations. This is a cross-cutting setting that affects shape
inference, guard generation, and code generation across the entire compilation
stack.

torch.compiler.config.enable_cpp_symbolic_shape_guards*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Uses C++ implementation for symbolic shape guard evaluation to improve performance.
The C++ guard manager can significantly speed up guard checking for symbolic shapes
in shape-polymorphic compilations.

torch.compiler.config.fail_on_recompile_limit_hit*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Raises a hard error when recompile limits are exceeded instead of falling back
to eager execution. This is useful for detecting excessive recompilation in
performance-critical deployments where you want to ensure compilation overhead
is kept under control.

torch.compiler.config.force_disable_caches*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Force disables all caching - This will take precedence over and override any other caching flag

torch.compiler.config.job_id*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)**= None*

Semantically, this should be an identifier that uniquely identifies, e.g., a
training job. You might have multiple attempts of the same job, e.g., if it was
preempted or needed to be restarted, but each attempt should be running
substantially the same workload with the same distributed topology. You can
set this by environment variable with `TORCH_COMPILE_JOB_ID`.

Operationally, this controls the effect of profile-guided optimization related
persistent state. PGO state can affect how we perform compilation across
multiple invocations of PyTorch, e.g., the first time you run your program we
may compile twice as we discover what inputs are dynamic, and then PGO will
save this state so subsequent invocations only need to compile once, because
they remember it is dynamic. This profile information, however, is sensitive
to what workload you are running, so we require you to tell us that two jobs
are *related* (i.e., are the same workload) before we are willing to reuse
this information. Notably, PGO does nothing (even if explicitly enabled)
unless a valid `job_id` is available. In some situations, PyTorch can be
configured to automatically compute a `job_id` based on the environment it
is running in.

Profiles are always collected on a per rank basis, so different ranks may have
different profiles. If you know your workload is truly SPMD, you can run with
`torch._dynamo.config.enable_compiler_collectives` to ensure nodes get
consistent profiles across all ranks.

torch.compiler.config.log_file_name*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)**= None*

Specifies a file path for TorchDynamo-specific logging output. When set, internal
TorchDynamo debug information is written to this file rather than stdout. This is
useful for debugging TorchDynamo's internal tracing behavior.

torch.compiler.config.recompile_limit*: [int](https://docs.python.org/3/library/functions.html#int)**= 8*

Maximum number of recompilations allowed for a single function before falling
back to eager execution. This compilation performance control prevents excessive
recompilation overhead that can degrade overall performance.

torch.compiler.config.reorderable_logging_functions*: [set](https://docs.python.org/3/library/stdtypes.html#set)**= {}*

A set of logging functions that can be reordered to execute after the compiled
portion of the graph, allowing larger graphs to be captured. Functions in this
set will have their execution deferred to avoid graph breaks, though this may
affect the timing of log output. In particular, mutated values will not be logged
at the right time, leading to incorrect logging.

torch.compiler.config.skip_tensor_guards_with_matching_dict_tags*: [bool](https://docs.python.org/3/library/functions.html#bool)**= True*

Optimizes guard generation by treating tensors as immutable when they are
dictionary values with consistent dictionary tags across invocations. This
reduces guard overhead for tensors stored in persistent data structures.

torch.compiler.config.verbose*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Enables verbose debugging output for Dynamo. When enabled, provides detailed
information about Dynamo's compilation decisions, optimizations, and potential
issues.

torch.compiler.config.wrap_top_frame*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

Wraps the top-level decorated function/module in a frame wrapper to ensure
nn.Module hooks are compiled within the same frame as the main function. This
improves compilation coverage for models that rely on hooks.