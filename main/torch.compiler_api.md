# torch.compiler API reference

For a quick overview of `torch.compiler`, see [torch.compiler](user_guide/torch_compiler/torch.compiler.html#torch-compiler-overview).

| [`compile`](generated/torch.compiler.compile.html#torch.compiler.compile) | See [`torch.compile()`](generated/torch.compile.html#torch.compile) for details on the arguments for this function. |
| --- | --- |
| [`reset`](generated/torch.compiler.reset.html#torch.compiler.reset) | Reset the in-process compiler state. |
| [`nonstrict_trace`](generated/torch.compiler.nonstrict_trace.html#torch.compiler.nonstrict_trace) | Decorator to mark a function as nonstrict-traceable for dynamo. |
| [`allow_in_graph`](generated/torch.compiler.allow_in_graph.html#torch.compiler.allow_in_graph) | Tells the compiler frontend (Dynamo) to skip symbolic introspection of the function and instead directly write it to the graph when encountered. |
| [`substitute_in_graph`](generated/torch.compiler.substitute_in_graph.html#torch.compiler.substitute_in_graph) | Register a polyfill handler for a function, usually a C function from the C extension, to be used in place of the original function when inlining the original function in the graph. |
| [`assume_constant_result`](generated/torch.compiler.assume_constant_result.html#torch.compiler.assume_constant_result) | This function is used to mark a function fn as having a constant result. |
| [`list_backends`](generated/torch.compiler.list_backends.html#torch.compiler.list_backends) | Return valid strings that can be passed to torch.compile(..., backend="name"). |
| [`disable`](generated/torch.compiler.disable.html#torch.compiler.disable) | This function provides a decorator to disable compilation on a function. |
| [`set_default_backend`](generated/torch.compiler.set_default_backend.html#torch.compiler.set_default_backend) | Set the default backend for `torch.compile` when no `backend` argument is specified. |
| [`get_default_backend`](generated/torch.compiler.get_default_backend.html#torch.compiler.get_default_backend) | Return the current default backend for `torch.compile`. |
| [`set_stance`](generated/torch.compiler.set_stance.html#torch.compiler.set_stance) | Set the current stance of the compiler. |
| [`set_enable_guard_collectives`](generated/torch.compiler.set_enable_guard_collectives.html#torch.compiler.set_enable_guard_collectives) | Enables use of collectives *during* guard evaluation to synchronize behavior across ranks. |
| [`cudagraph_mark_step_begin`](generated/torch.compiler.cudagraph_mark_step_begin.html#torch.compiler.cudagraph_mark_step_begin) | Indicates that a new iteration of inference or training is about to begin. |
| [`cudagraph_mark_warmup_incomplete`](generated/torch.compiler.cudagraph_mark_warmup_incomplete.html#torch.compiler.cudagraph_mark_warmup_incomplete) | Request another warmup for the active CUDA Graph Trees function. |
| [`is_compiling`](generated/torch.compiler.is_compiling.html#torch.compiler.is_compiling) | Indicates whether a graph is executed/traced as part of torch.compile() or torch.export(). |
| [`is_dynamo_compiling`](generated/torch.compiler.is_dynamo_compiling.html#torch.compiler.is_dynamo_compiling) | Indicates whether a graph is traced via TorchDynamo. |
| [`is_exporting`](generated/torch.compiler.is_exporting.html#torch.compiler.is_exporting) | Indicates whether we're under exporting. |
| [`keep_portable_guards_unsafe`](generated/torch.compiler.keep_portable_guards_unsafe.html#torch.compiler.keep_portable_guards_unsafe) | A common function to only keep guards that can be used in both Python and non-Python environments. |
| [`skip_guard_on_inbuilt_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe.html#torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe) | A common function to skip guards on the inbuilt nn modules like torch.nn.Linear. |
| [`skip_guard_on_all_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_all_nn_modules_unsafe.html#torch.compiler.skip_guard_on_all_nn_modules_unsafe) | A common function to skip guards on all nn modules, both user defined as well inbuilt nn modules (like torch.nn.Linear). |
| [`keep_tensor_guards_unsafe`](generated/torch.compiler.keep_tensor_guards_unsafe.html#torch.compiler.keep_tensor_guards_unsafe) | A common function to keep tensor guards on all tensors. |
| [`skip_guard_on_globals_unsafe`](generated/torch.compiler.skip_guard_on_globals_unsafe.html#torch.compiler.skip_guard_on_globals_unsafe) | A common function to skip guards on all globals. |
| [`skip_all_guards_unsafe`](generated/torch.compiler.skip_all_guards_unsafe.html#torch.compiler.skip_all_guards_unsafe) | A function for skipping all guards on a compiled function. |
| [`nested_compile_region`](generated/torch.compiler.nested_compile_region.html#torch.compiler.nested_compile_region) | Tells **``torch.compile``** that the marked set of operations forms a nested compile region (which is often repeated in the full model) whose code can be compiled once and safely reused. |
| [`load_cache_artifacts`](generated/torch.compiler.load_cache_artifacts.html#torch.compiler.load_cache_artifacts) | Hot loads cache artifacts that were previously serialized via save_cache_artifacts |
| [`load_compiled_function`](generated/torch.compiler.load_compiled_function.html#torch.compiler.load_compiled_function) | Load an aot-compiled function from a file. |
| [`save_cache_artifacts`](generated/torch.compiler.save_cache_artifacts.html#torch.compiler.save_cache_artifacts) | Serializes all the cache artifacts that were created during the compilation |
| [`wrap_numpy`](generated/torch.compiler.wrap_numpy.html#torch.compiler.wrap_numpy) | Decorator that turns a function from `np.ndarray`s to `np.ndarray`s into a function from `torch.Tensor`s to `torch.Tensor`s. |

## torch.compiler.precompile

Warning

`torch.compiler.precompile` and everything reached through it is a prototype API.
Signatures, error types and the artifact format may change between releases without a
deprecation cycle.

`torch.compiler.precompile` captures a whole computation - `fn(model, x)`, with the
model(s) passed as arguments - ahead of time from the caller's own calls, and lowers it to
a self-contained Python source artifact plus an acceleration cache that a fresh process
reloads. No weights are baked in, so the model is passed again at runtime:

```
with torch.compiler.precompile.capture(
 lambda model, x: model(x), artifact_path="m.py", cache_path="m.cache"
) as cap:
 y = cap(model, x)

f = torch.compiler.precompile.load("m.py", "m.cache")
y = f(model, x)
```

The contract is Note [precompile programming model] in `torch/_precompile.py`. It is
distinct from `torch._dynamo.config.caching_precompile` (a `torch.compile` caching mode).

torch.compiler.precompile.capture(*fn*, */*, ***, *artifact_path*, *cache_path*, *tracer=MakeFxTracer(decompositions=None)*, *backend='inductor'*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/_precompile.py#L2694)

Capture `fn` across the calls YOUR loop makes, writing the artifact on exit.

Warning

This is a prototype API. Its signature, error types and artifact
format may change between releases without a deprecation cycle.

Capture is caller-driven: this returns a capture object rather than running
anything. Enter it as a context manager, call it exactly as you would `fn`
inside the block (a `MakeFxTracer` capture takes exactly one call) -
each call runs for real, folds what it exercised into the capture, and
returns that run's result - and the `(python_code, cache)` artifact is
written to `artifact_path` / `cache_path` when the block exits:

```
with torch.compiler.precompile.capture(
 fn, artifact_path="m.py", cache_path="m.cache"
) as cap:
 y = cap(model, x)
f = torch.compiler.precompile.load("m.py", "m.cache")
```

Because the caller makes the calls, inputs flow through naturally and return
values stay available, so the capture drops into an ordinary pipeline loop.
To write the artifact before the block ends, call `cap.save()` inside it.
A block that raises writes nothing it has not already saved, and a block
that made no call raises `PrecompileError` on exit. A capture is single-use:
to capture again, call `capture()` again.

`tracer` picks the capture front-end and carries its tracer-specific
configuration. `MakeFxTracer` is one non-strict ATen trace: the capture
takes exactly ONE call, refuses a second, and specializes control flow and
shapes to that call, with the contract of Note [precompile programming model]
in `torch/_precompile.py`. Arguments are matched positionally at capture and
at load. `fn` is the whole computation, e.g. `lambda model, x: model(x)`:
the `nn.Module` arguments have their params/buffers lifted to graph inputs
(no weights are baked in) and the rest are the runtime inputs; the reloaded
callable is invoked with the same argument structure, and the runtime model
must match the captured model's parameter/buffer structure.

`backend` selects how the captured graph is realized: `"inductor"`
(default) lowers through AOTAutograd + Inductor into one self-contained
module, and the cache holds the bundle that primes the inductor kernel caches
on load; `"eager"` keeps the captured ATen graph and runs it as-is (no
kernels, so the cache carries no artifact). A `fn` that runs a backward
captures it: the trace runs with grad enabled, the resulting parameter
gradients are scattered onto the runtime model exactly like eager
`.backward()`, and the artifact returns `fn`'s own result.

Note

`torch.compiler.precompile` is NOT
`torch._dynamo.config.caching_precompile` (a `torch.compile`
guard-serialization caching mode); it captures `fn` ahead of time and
lowers it to a self-contained Python source artifact.

Return type:

*Capture*

torch.compiler.precompile.load(*artifact_path*, *cache_path*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/_precompile.py#L2779)

Reconstruct a runnable from the two files a precompile capture wrote.

Warning

This is a prototype API. Its signature, error types and artifact
format may change between releases without a deprecation cycle.

Name the two files `capture()` wrote - the `python_code` artifact and
its `cache`. A readable, current-format cache loads only
against the `python_code` it was emitted with (it carries a sha256 of exactly
those bytes); an unreadable or other-format cache is ignored with a warning.

The driver runs from `python_code` - the single source of truth for the whole
calling convention. `load` reads the source's `BACKEND`, checks the cache's
`backend` tag against it, primes the inductor kernel caches when the cache
carries a bundle so a warm reload loads precompiled kernels instead of
JIT-compiling, and then exec's `python_code`. With no usable cache it degrades to JIT'ing from
`python_code`. Both files are trusted, EXECUTABLE input: load only artifacts
you produced or otherwise trust.

Call the result with the SAME argument structure `fn` took - the model(s)
in their original positions plus the runtime inputs. The runtime model must
match the captured model's parameter/buffer structure; precompile re-derives
the param/buffer list from it. The result is a
`torch.compiler.precompile.PrecompiledRunnable`.

Raises `PrecompileError` if either file cannot be read, if `python_code` is
not a `torch.compiler.precompile` artifact, or if the cache's `backend` or
`code_hash` does not match `python_code` - the pair came from different
captures. A cache whose `format`/`version` does not match (a foreign or
different-build envelope) is NOT fatal: the cache is acceleration only, so
`load` degrades to JIT'ing from `python_code` rather than crashing.

Return type:

*PrecompiledRunnable*

*exception*torch.compiler.PrecompileError

The error type raised by `torch.compiler.precompile` and its artifacts.

Raised when capture, lowering, `load`, or a runtime call violates the precompile
contract - e.g. a tensor baked as a constant (invariant 1), an unsupported /
effectful op, a nested example input, which capture does not support on either path
(invariant 3), an UNBACKED capture attempted inside another trace (invariant 3), a
non-tensor output the inductor backend cannot lower, or a runtime input whose shape or
memory format differs from the example (invariants 3 and 6).
See Note [precompile programming model] in this module for the full contract.

*class*torch.compiler.precompile.MakeFxTracer(*decompositions=None*)

The `make_fx` capture front-end, passed as `tracer=` to a precompile capture.

A NON-STRICT single make_fx trace: it records the ATen ops of ONE execution of
`fn`, so a `capture` with this tracer takes exactly one call and refuses a
second, and control flow and shapes are specialized to that call (the source of
the programming-model contract). Part of the prototype `torch.compiler.precompile`
API, so it may change without a deprecation cycle.

The contract in brief (Note [precompile programming model] in
`torch/_precompile.py` has the full list): every tensor `fn` reads is an
argument or a registered parameter/buffer of an `nn.Module` argument, and
shapes are static unless a dim is marked with `mark_unbacked`
(`torch._dynamo.decorators`, inductor backend only) before the call: a
marked dim is captured as an unbacked symint, so one artifact serves any
runtime size of it, and a graph that needs to guard on it fails at capture.
Dims that must be equal at runtime must share a `shape_id`: marked
independently they bake a silent equal-size assumption, and a mismatch at
runtime is not caught. Each input's dtype and device are specialized too (a
runtime mismatch is rejected), the inductor backend additionally specializes
on memory format, and a nested-tensor example input is refused.

`decompositions` is an optional decomposition table (a dict mapping each
`OpOverload` to a decomposition function) forwarded to `make_fx` as its
`decomposition_table`; it is specific to this tracer (Dynamo lowers through the
backend instead).

*class*torch.compiler.precompile.Capture

The caller-driven capture `torch.compiler.precompile.capture` returns.

Part of the prototype `torch.compiler.precompile` API, so it may change
without a deprecation cycle. Enter it as a context manager to arm the
capture, call it exactly as you would `fn` inside the block - each call
runs for real, is folded into the capture, and returns that run's result
- and the artifact is written to the `artifact_path` / `cache_path`
files when the block exits. How many calls a capture takes is the tracer's:
`MakeFxTracer` takes exactly one. Call `save()` inside the block
to write what has been captured so far to those same files without ending
the capture. A block that raises writes nothing it has not already saved,
and a block that made no call raises `PrecompileError` on exit rather
than writing an empty artifact. A capture is single-use: once its block
exits it cannot be entered again, so call `capture()` again to retry.
That includes a failed write at exit: the spent capture does not keep its
pair, so fix the path and capture again.

save()[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/_precompile.py#L423)

Write everything captured so far to the artifact files without ending the capture.

Raises `PrecompileError` outside the capture's `with` block.

*class*torch.compiler.precompile.PrecompiledRunnable

What `torch.compiler.precompile.load` returns.

A callable with the captured `fn`'s calling convention that can also be
entered as a context manager and unloaded. A standalone artifact installs
nothing, so for it `__enter__`/`__exit__`/`unload()` are no-ops.
Part of the prototype `torch.compiler.precompile` API, so it may change
without a deprecation cycle.

Variables:

**installed** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether calling this handle installs onto the captured code
objects; `False` for a standalone artifact.

unload()[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/_precompile.py#L391)

Remove whatever this loaded artifact installed; a no-op when it installed nothing.

*class*torch.compiler.precompile.PrecompileSummary(***, *frames*, *resume_functions*, *guarded_codes*, *backend_graphs*, *bypassed=()*, *truncated=()*, *uncovered_frames=()*, *wont_generalize=()*, *dropped_guards=()*, *kept_guards=()*, *risky_dropped_guards=()*, *policy_dropped_guards=()*, *dropped_guard_code=()*, *capture_errors=()*)

Coverage and guard information from an observed precompile capture.

`str(summary)` renders a one-line digest: the counts, the dropped guards
tallied by type, the risky slots and frame lists cut to their first five
entries (`+N more`), and the first non-empty line of the first capture
error.
Everything here describes the calls that ran, not every possible input or
unexecuted branch, and once `truncated` is non-empty every count and
frame list is a lower bound: from a limit hit on, that frame and everything
it called ran untraced, so a frame first reached there is in no list here.

The guard fields hold `(guard_type, source)` slots, the source spelled
with the local scope stripped (`L['self'].act` -> `self.act`;
`G['CFG'].width` unchanged). Each list holds a slot once, however many
frames or variants carried it, so `dropped_guard_types` counts distinct
slots, not occurrences. The relations between the lists hold within one
frame variant, where the producer applies them, and are stated here rather
than checked:

- `kept_guards` and `dropped_guards` are disjoint: the filter gives a
slot one verdict, keep or reject.
- `risky_dropped_guards` is drawn from `dropped_guards`.
- `policy_dropped_guards` is disjoint from both: a policy drop is taken
out of the serialized copy the filter kept, once the slot held
identically across every captured variant, and is not checked either.
- `dropped_guard_code` draws its slots from `dropped_guards` and
`policy_dropped_guards`.
- every `wont_generalize` source is the source half of a `kept_guards`
slot, the value-equality guard that pins it.

The lists aggregate every captured frame and a slot names no frame, so two
frames' `self.act` are one slot: a slot one frame kept and another dropped
is in both `kept_guards` and `dropped_guards` (the digest's `(N kept)`
is the kept count beside the drops, not the other half of a total), and a
slot one frame's filter rejected and another frame's invariance policy
dropped is in both drop lists. Nothing is enforced, as for the frame lists
below: a report that raised on its own bookkeeping would lose the coverage
it exists to describe.

The frame lists differ in what an entry is. `bypassed` and
`uncovered_frames` hold one bare `co_name` per frame, read off the
package's entries, so a name can repeat (every `nn.Module` has a
`forward`: `['forward', 'forward']` is two frames, not a repeat) and
their lengths count frames. `truncated` holds `co_name
(filename:firstlineno)`, recorded once per code object that hit the limit,
so its entries do identify a frame. A bare name identifies none, so the two
bare lists cannot be checked disjoint.

Variables:

- **frames** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Captured frames: every frame the package holds an entry for, the
`bypassed`, `truncated` and `uncovered_frames` ones included,
so the digest's frame clauses cut into this count rather than add
to it.
- **resume_functions** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Of those, the graph-break continuations.
- **guarded_codes** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Guarded code objects across all frames.
- **backend_graphs** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Compiled backend graphs.
- **bypassed** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - The `co_name` of each frame the package holds nothing
servable for: no compile of the frame recorded a guarded code and
one was bypassed (its guards could not be serialized, or its graph
held parameters by static address), or a backend artifact was
missing when the package was saved. Not an eager fallback: the
frame ran compiled during capture, but the package kept no variant
of it a load can serve, so a call that reaches it raises.
- **truncated** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - `co_name (filename:firstlineno)` of each frame that hit the
recompile limit. A lower bound, which is why the digest prints it
as `>=`: from a limit hit on, that frame and the frames it calls
run without tracing, so a limit hit that would follow it there is
never recorded.
- **uncovered_frames** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - The `co_name` of each frame the capture ran that
ended with no guarded code and was not bypassed, so the artifact
cannot serve it: a thin wrapper whose graphs all landed in an inner
frame, a frame Dynamo gave up on, or a frame whose compile raised
(its message is in `capture_errors`, so one failure shows in both
digest clauses). A different cause from `bypassed`,
never the same frame; a frame that hit the recompile limit before it
recorded a guarded code is in `truncated` too. Not a remainder:
which frames count as a gap is the producer's decision, and a frame
the package holds an entry for but never ran is not one, so this is
not `frames` minus `bypassed` minus the frames that hold guarded
code.
- **wont_generalize** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - Guard *sources* (not frame names) a kept value-equality
guard on a bare argument name pins in some variant (`self.eps` is
not a bare name) while no other variant of the same frame guards the
source without pinning it, so as captured no variant served another
value. Observed, not proven: a variant that never guarded the source
does not count as serving other values of it.
- **dropped_guards** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*]**,**...**]*) - Slots the serialized copy's guard filter rejected; a
variant that dropped a slot does not check it, so a load through
that variant cannot notice whatever it checked. The default filter
drops a guard when the serializer refuses its type or a type its
check derives: the identity guards (`ID_MATCH`,
`FUNCTION_MATCH`, `NN_MODULE` and the like), `WEAKREF_ALIVE`
and most `DICT_VERSION` guards, so a load cannot notice that the
objects they checked were rebound, mutated or collected. Passing it
does not make a guard serializable; a caller-supplied filter decides
its own set. A slot is listed under the guard's own type whatever
the reason for the drop, so a `TENSOR_MATCH` rejected for what its
check derives is a dropped `TENSOR_MATCH`.
- **kept_guards** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*]**,**...**]*) - Slots the serialized copy's guard filter kept and the
invariance policy left in place.
- **risky_dropped_guards** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*]**,**...**]*) - The subset of `dropped_guards` observed to tell
captured variants apart, or flagged by the risky-drop lint as a
configuration-chosen binding.
- **policy_dropped_guards** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*]**,**...**]*) - Slots the filter kept that the invariance policy
then dropped because they held identically across every captured
variant (only guard types from a fixed set are eligible). Reported
apart from `dropped_guards` because the remedy differs, and
reported at all because a capture that discards a precondition
should not look like one that had none.
- **dropped_guard_code** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*]**,**...**]*) - `(guard_type, source, rendered_check)`, one per
slot of `dropped_guards` or `policy_dropped_guards` whose guard
rendered a check (how a guard is installed does not predict whether
it renders one, and a slot whose guard rendered none has no entry).
One rendering however many variants dropped the slot: where the
check embeds the guarded value (`EQUALS_MATCH` renders
`L['n'] == 3`) it is one variant's, the producer's pick rather
than a merge, so it tells the form of the check and not the value;
that the slot varied at all is what `risky_dropped_guards`
records. Carried because a slot alone can be ambiguous: a dropped
`('HASATTR', "counts['pixel']")` is either the benign companion of
a kept `TENSOR_MATCH` on the same source or the only guard on an
optional attribute, and only the rendered check tells them apart.
Kept beside the slot lists so the slots stay the identity the policy
compares on; for programmatic consumers, not the digest.
- **capture_errors** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - One message per distinct exception a capture call raised
(repeats of the same type and message collapse), the exception type
first (`"RuntimeError: boom"`), so the digest's first line is
never empty however the exception was raised.

*property*complete*: [bool](https://docs.python.org/3/builtins/functions.html#bool)*

Whether the capture covers everything it exercised.

Coverage only: False if a frame was `bypassed`, hit the recompile
limit (`truncated`) or ended with no guarded code
(`uncovered_frames`), if a capture call raised (`capture_errors`),
or if nothing was compiled. Both `guarded_codes` and `backend_graphs`
must be non-zero for the last check, because a frame that compiled
nothing can still count as one guarded code, so `guarded_codes` alone
cannot tell a real capture from an empty one.
The guard fields never enter: `risky_dropped_guards` is a lint
finding, not a proof, and `wont_generalize` follows from any value the
capture pinned, so both describe how far a complete capture generalizes
and the digest reports them on their own.

*property*dropped_guard_types*: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [int](https://docs.python.org/3/builtins/functions.html#int)]*

The distinct dropped slots counted by guard type.

*property*kept_guard_types*: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [int](https://docs.python.org/3/builtins/functions.html#int)]*

The distinct kept slots counted by guard type.