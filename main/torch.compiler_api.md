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
# step is a module-level function: def step(model, x): return model(x)
with torch.compiler.precompile.capture(
 step, artifact_path="m.py", cache_path="m.cache"
) as cap:
 y1 = cap(model, x1)
 y2 = cap(model, x2) # a recompile or graph break becomes another variant

f = torch.compiler.precompile.load("m.py", "m.cache") # in a fresh process
y = f(model, x1)
```

The default `DynamoTracer` records every frame Dynamo compiles while your calls run and
the artifact dispatches among them by their guards; `MakeFxTracer` is a single non-strict
trace under the contract of Note [precompile programming model] in `torch/_precompile.py`.
`torch.compiler.precompile` is distinct from `torch._dynamo.config.caching_precompile`
(a `torch.compile` caching mode).

torch.compiler.precompile.capture(*fn*, */*, ***, *artifact_path*, *cache_path*, *tracer=DynamoTracer(guard_filter_fn=None, recompile_limit=256, dynamic=None, require_complete=True, require_no_risky_drops=True)*, *backend='inductor'*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/_precompile.py#L3311)

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
to capture again, call `capture()` again. A `DynamoTracer` capture
records the kernel-cache artifacts of everything compiled inside the block,
so compile nothing else there, and do not overlap two such captures. Only
what runs inside the block is carried: run every kernel the serving process
needs there, since one compiled or launched only before the block is not in
the cache. Each write also freezes the compiled kernels the serving process
needs, and raises `PrecompileError` for one it cannot
freeze. That includes kernels launched directly through `@triton.jit` and
`@triton.autotune` inside the block: Triton compiles into a fresh cache
directory there, with its autotuning cache on, so a `TRITON_CACHE_DIR`
you set is not used inside the block, and a JIT kernel or autotuner already
used before the block compiles and tunes again on its first launch inside
it. That retune benchmarks on the block's real inputs, and the config it
picks, which is what ships and what the process keeps using afterwards, may
differ from the one picked before the block. Compiled JIT kernel
specializations and autotuning decisions the block does not produce again
are kept afterwards.
Triton does not cache the decision of an autotuner with `pre_hook`
configs, so one that does not prune its configs keeps its earlier decision
in the block and is benchmarked again on first use in the serving process.
No other thread should launch Triton kernels while the block opens or
closes: the in-memory caches are dropped and restored then without
synchronizing with launches, so a concurrent autotuner launch can fail.
Triton kernels another thread compiles or tunes while the block is open
go into the block's cache directory and ship with it.

`tracer` picks the capture front-end and carries its tracer-specific
configuration. `DynamoTracer` (the default) is an execution-driven
multi-graph capture: it analyzes the Python rather than tracing one path,
records every graph-break continuation and guarded recompilation the calls
exercise, takes as many calls as you make (keyword arguments included), and
the artifact dispatches among the captured variants by their guards - a
call no variant covers RAISES rather than silently serving, since there is
no compiler behind a source artifact, unless Dynamo gave up on that frame
during the capture (`PrecompileSummary.eager_fallbacks`): the capture ran
that frame eagerly, so the call runs eagerly too. `MakeFxTracer` is
one non-strict ATen trace: the capture takes exactly ONE positional call,
refuses a second, and specializes control flow and shapes to that call, with
the contract of Note [precompile programming model] in
`torch/_precompile.py`. `fn` is the whole computation, e.g. a
module-level `def step(model, x): return model(x)` (only a
`MakeFxTracer` capture also takes a lambda): the `nn.Module`
arguments have their params/buffers lifted to graph inputs (no weights are
baked in) and the rest are the runtime inputs; the reloaded callable is
invoked with the same argument structure, and the runtime model must match
the captured model's parameter/buffer structure.

A Dynamo artifact is STANDALONE: it rebuilds the entry from its code object
and installs nothing, so `fn` must be a module-level function of an
importable module (not a closure, not defined in `__main__`). The
exception is a capture that compiled a frame the entry cannot reach through
a graph-break continuation - a graph break inside a child module's forward:
its artifact has `SERVING_MODE = "installed"` and serves by installing the
captured entries onto the live code objects when loaded. It is locked
to the producing Python version and torch build. The guards that could not
be serialized are reported in the capture's `summary()` rather than
checked, and the `DynamoTracer` `require_*` gates refuse the risky
ones by default.

`backend` selects how the captured graph is realized: `"inductor"`
(default) lowers through AOTAutograd + Inductor into one self-contained
module, and the cache holds the bundle that primes the inductor kernel caches
on load; `"eager"` keeps the captured ATen graph and runs it as-is (no
kernels, so the cache carries no artifact). A make_fx `fn` that runs a
backward captures it: the trace runs with grad enabled, the resulting
parameter gradients are scattered onto the runtime model exactly like eager
`.backward()`, and the artifact returns `fn`'s own result. A Dynamo
capture runs every call in the caller's own grad mode and lowers a backward
whenever grad is enabled (a `.backward()` in `fn` graph-breaks and
re-runs at serve time through the live autograd engine, accumulating
`.grad` like eager); serve the artifact under the grad mode it was
captured in.

Note

`torch.compiler.precompile` is NOT
`torch._dynamo.config.caching_precompile` (a `torch.compile`
guard-serialization caching mode); it captures `fn` ahead of time and
lowers it to a self-contained Python source artifact.

Return type:

*Capture*[~_P, *_R*]

torch.compiler.precompile.load(*artifact_path*, *cache_path*, ***, *allow_serve_time_compiles=False*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/_precompile.py#L3474)

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
JIT-compiling, and then exec's `python_code`. With no usable cache a
`MakeFxTracer` artifact degrades to JIT'ing from `python_code`; a
`DynamoTracer` artifact carries its compiled subgraphs inside
`python_code`, with their kernels under inductor's default bundling, so it
serves without JIT either way. Both files are trusted, EXECUTABLE input: load
only artifacts you produced or otherwise trust.

Call the result with the SAME argument structure `fn` took - the model(s)
in their original positions plus the runtime inputs (keyword arguments too,
for a `DynamoTracer` artifact). The runtime model must match the
captured model's parameter/buffer structure. The result is a
`torch.compiler.precompile.PrecompiledRunnable`; a Dynamo artifact
is standalone, so entering and unloading it are no-ops, and it re-seeds the
names Dynamo minted into the captured module. The exception is a capture that
compiled a frame the entry reaches only by an ordinary call (a graph break
inside a child module's forward): its artifact has `SERVING_MODE =
"installed"` and serves by installing the captured entries onto the live
code objects; its calls refuse to compile, as under the `fail_on_recompile`
stance, without setting that process-wide stance, and keep refusing under
every process-wide stance that would compile (`force_backend`,
`"eager_then_compile"`, ...). Under `"force_eager"` every call runs
eagerly, bypassing the installed entries; under `"eager_on_recompile"` the
captured variants are served and any other call runs eagerly. An installed
artifact refuses to load with `torch._dynamo.config.compiled_autograd`
enabled, which would compile backward graphs outside it, and with Dynamo
disabled (`TORCHDYNAMO_DISABLE=1` or the `enable_dynamo` killswitch),
which it serves through. A Dynamo artifact whose
capture graph-broke cannot load beside the live compile that captured it
(the continuation names collide), and an installed artifact is refused
wherever any frame it installs onto already has live Dynamo cache entries:
load it in a fresh process. That check runs only at load: compiling those
frames after load adds live entries that serve the calls the installed
ones miss.

Either kind of artifact runs a call eagerly instead of refusing it when the
missed frame is one Dynamo gave up on during the capture (listed in
`PrecompileSummary.eager_fallbacks` and marked `# eager fallback` in the
artifact's `FRAMES`), since the capture ran that frame eagerly too. A
frame that kept variants logs a warning the first time a call misses them;
one that compiled none is served as plain Python from the start, as a
trivial frame is, with no warning, since there is no compiled code to lose.
Under an installed artifact only that frame runs eagerly: the frames it
calls still dispatch to their own variants. A standalone artifact installs
nothing, so the rest of the call from that frame on, its callees included,
runs as plain Python; whatever ran before it, such as the entry's variant
up to a graph break whose continuation fell back, still ran compiled.

Frozen C++ kernels are keyed by their full build command, which includes
the producer's absolute PyTorch include and library paths, so they serve
only a host whose PyTorch install and toolchain paths match the producer's.
Any other host rebuilds them, which needs a C++ compiler there:
`no_compilation()` does not gate C++ builds.

`allow_serve_time_compiles=True` opts an installed artifact out of the
refusal: a call no captured variant covers compiles with the artifact's
backend, as `torch.compile` would, under the process-wide stance like any
other compile. The captured variants are still served first and do not
count toward `torch._dynamo.config.recompile_limit`, so each frame gets
that many serve-time compiles on top of them; a missed call past the limit
runs eagerly instead of compiling.
Serve-time compiles are recorded nowhere, but they are built under the
process's Dynamo config: with `torch._dynamo.config.caching_precompile` on
they drop identity guards (`ID_MATCH`, `CLOSURE_MATCH`, ...) exactly as
any other compile in that process does.
The flag does not lift the `compiled_autograd` refusal above. A standalone
artifact has no compiler behind it, and an installed artifact captured
before the flag existed cannot honor it, so passing the flag for either
raises `PrecompileError`.

Raises `PrecompileError` if either file cannot be read, if `python_code` is
not a `torch.compiler.precompile` artifact, or if the cache's `backend`,
`tracer` or `code_hash` does not match `python_code` - the pair came from different
captures - or if an installed artifact cannot install onto the serving process (for
example, a captured source changed since capture). A cache whose `format`/`version` does not match (a foreign or
different-build envelope) is NOT fatal: the cache is acceleration only, so
`load` degrades to JIT'ing from `python_code` rather than crashing.

Return type:

*PrecompiledRunnable*

torch.compiler.precompile.no_compilation()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/_precompile.py#L3173)

Forbid graph/kernel compilation and autotuning on every thread of this process.

Use it around a serving worker's lifetime to prove that a loaded artifact
and its kernel/autotune cache cover every execution: anything that would
trace a graph, compile a kernel, benchmark or autotune raises
`PrecompileError` instead of silently compiling:

```
runnable = torch.compiler.precompile.load(artifact_path, cache_path)
with torch.compiler.precompile.no_compilation():
 serve(runnable) # raises rather than compiling on a cache miss
```

Only kernels already in the in-process kernel cache may run.

Unlike `precompile.serving()`, which is thread-local, the policy is
process-wide. Nested and overlapping uses are depth-counted, so it stays
active until the last owner exits; callers must drain work they dispatched
(e.g. to compile workers) before that exit. While active,
`TORCH_PRECOMPILE_NO_COMPILATION=1` is exported so child processes
inherit it, and setting exactly `"1"` before startup enables the policy
for the whole process.

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)[None]

*exception*torch.compiler.PrecompileError

The error type raised by `torch.compiler.precompile` and its artifacts.

Raised when capture, lowering, `load`, or a runtime call violates the precompile
contract - e.g. a tensor baked as a constant (invariant 1), an unsupported /
effectful op, a nested example input, which capture does not support on either path
(invariant 3), an UNBACKED capture attempted inside another trace (invariant 3), a
non-tensor output the inductor backend cannot lower, or a runtime input whose shape or
memory format differs from the example (invariants 3 and 6).
See Note [precompile programming model] in this module for the full contract.

*class*torch.compiler.precompile.DynamoTracer(*guard_filter_fn=None*, *recompile_limit=256*, *dynamic=None*, *require_complete=True*, *require_no_risky_drops=True*)

The `dynamo` capture front-end (the default), passed as `tracer=` to
`torch.compiler.precompile.capture()`.

An execution-driven multi-graph capture that analyzes the Python (bytecode)
rather than tracing one path: it records graph-break continuations and every
guarded recompilation the calls exercise, so a capture with this tracer takes
as many calls as you make, keyword arguments included. Part of the prototype
`torch.compiler.precompile` API, so it may change without a deprecation cycle.

`guard_filter_fn` takes the `GuardFilterEntry` records (`guard_type`,
`name`, ...) and returns one keep flag per entry. It filters the runtime
guards during capture as well as the serialized ones (the default drops only
what cannot be serialized), so a dropped guard never triggers a recompile during
capture; `recompile_limit` caps recompilations per frame, and a call past it
runs eager and is absent from the artifact without any gate refusing it;
`dynamic` forces dynamic shapes as `torch.compile(dynamic=)` does. The
`require_*` gates refuse, at write time, an artifact with a coverage gap
(`require_complete`: a bypassed or uncovered frame, a call that raised) or one
whose dropped guards told captured variants apart or hang off a
configuration-chosen slot (`require_no_risky_drops`). Other dropped guards,
such as the identity guards every model drops because they cannot be serialized,
are listed in the artifact rather than refused.

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

save()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/_precompile.py#L518)

Write everything captured so far to the artifact files without ending the capture.

Each call re-renders and rewrites both files, so a job that dies between
saves leaves the last checkpoint loadable. A refusal (such as a
`DynamoTracer` `require_*` gate) or a failed write raises but
writes nothing partial, and the capture stays open. Raises
`PrecompileError` outside the capture's `with` block.

*class*torch.compiler.precompile.PrecompiledRunnable

What `torch.compiler.precompile.load` returns.

A callable with the captured `fn`'s calling convention that can also be
entered as a context manager and unloaded. A standalone artifact installs
nothing, so for it `__enter__`/`__exit__`/`unload()` are no-ops.
Removing an installed artifact's entries is not implemented yet either, so
they stay installed until the process exits: serve an installed artifact
from a process you can throw away.
Part of the prototype `torch.compiler.precompile` API, so it may change
without a deprecation cycle.

Variables:

**installed** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether loading this artifact installed onto the captured
code objects (`SERVING_MODE = "installed"`); `False` for a
standalone artifact.

unload()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/_precompile.py#L460)

Remove whatever this loaded artifact installed; currently a no-op in every mode.

*class*torch.compiler.precompile.PrecompileSummary(***, *frames*, *resume_functions*, *guarded_codes*, *backend_graphs*, *bypassed=()*, *truncated=()*, *uncovered_frames=()*, *eager_fallbacks=()*, *wont_generalize=()*, *dropped_guards=()*, *kept_guards=()*, *risky_dropped_guards=()*, *policy_dropped_guards=()*, *dropped_guard_code=()*, *capture_errors=()*)

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
it exists to describe. The one exception to "every captured frame" is a
frame the artifact runs as plain Python (see `frames`): its guards are left
out, so a slot only such frames kept, dropped or riskily dropped is not in
that list.

The frame lists differ in what an entry is. `bypassed` and
`uncovered_frames` hold one bare `co_name` per frame, read off the
package's entries, so a name can repeat (every `nn.Module` has a
`forward`: `['forward', 'forward']` is two frames, not a repeat) and
their lengths count frames. `truncated` and `eager_fallbacks` hold
`co_name (filename:firstlineno)`, once per code object, so their entries
do identify a frame. A bare name identifies none, so the two
bare lists cannot be checked disjoint.

Variables:

- **frames** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Captured frames: every frame the package holds an entry for, the
`bypassed`, `truncated`, `uncovered_frames` and
`eager_fallbacks` ones included, so the digest's frame clauses
cut into this count rather than add to it. Also included are the
frames the artifact deliberately runs as plain Python: a frame
other than the entry that compiled no graph or graph-break
continuation and either lost a guard to the filter or was
bypassed. Running its original bytecode gives up no compiled
code, so it is served that way rather than through a variant
missing a guard, and it is listed in neither `bypassed` nor
`uncovered_frames`.
- **resume_functions** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Of those, the graph-break continuations.
- **guarded_codes** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Guarded code objects across all frames.
- **backend_graphs** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Compiled backend graphs.
- **bypassed** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - The `co_name` of each frame the package holds nothing
servable for: no compile of the frame recorded a guarded code and
one was bypassed (its guards could not be serialized, or its graph
held parameters by static address), or a backend artifact was
missing when the package was saved. A graphless frame run as plain
Python (see `frames`) is not listed. Not an eager fallback: the
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
frame, a frame whose compile raised (its message is in
`capture_errors`, so one failure shows in both digest clauses), a
frame whose compile error `suppress_errors=True` swallowed, or an
entry frame Dynamo gave up on at its first call. A different cause
from `bypassed`, never the same frame; a frame that hit the
recompile limit before it recorded a guarded code is in
`truncated` too. Not a remainder: which frames count as a gap is
the producer's decision, and a frame the package holds an entry for
but never ran is not one, so this is not `frames` minus
`bypassed` minus the frames that hold guarded code.
- **eager_fallbacks** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**...**]*) - `co_name (filename:firstlineno)` of each frame Dynamo
gave up on during the capture and skipped for the rest of it, for
any of Dynamo's soft reasons: a graph break it could
not resume from (such as one inside a loop), a
`torch._dynamo.skip_frame()` call, a frame it refuses to trace, a
`UserError` it suppressed by skipping the frame, or a backend that
declined the graph by raising `SkipFrame` or failed on it with an
error Dynamo falls back on (such as
`DynamicOutputShapeException`). A compile error
`suppress_errors=True` swallows is not one: Dynamo skips that
frame too, but it stays in `uncovered_frames` so the failure is
seen. Not a gap, and not in `uncovered_frames`: a load serves the
variants its earlier calls compiled and runs any call they miss
eagerly, logging a warning once per frame (the capture skipped every
later call, even one a variant matches). A frame that compiled no
variant is served as plain Python from the start, as a trivial frame
is, with no warning. The exception is an entry frame that fell back
on its first call, such as an entry generator, which Dynamo refuses
before tracing: it has no variant to dispatch to, so it is in
`uncovered_frames` instead.
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
or if nothing was compiled. `eager_fallbacks` never makes a capture
incomplete: a load runs those frames eagerly, as Dynamo chose to (an
entry frame with no variant is not one, see `uncovered_frames`). Both
`guarded_codes` and `backend_graphs` must be non-zero for the last
check, because a frame that compiled nothing can still count as one
guarded code, so `guarded_codes` alone cannot tell a real capture
from an empty one.
Nor does it promise that a load serves every call the capture ran: once
a frame falls back, the capture runs its later calls eagerly, even one
an earlier variant matches, and records nothing past it. A load serves
such a call through that variant, and a continuation or callee it then
reaches may have no variant for it and refuse the call.
The guard fields never enter: `risky_dropped_guards` is a lint
finding, not a proof, and `wont_generalize` follows from any value the
capture pinned, so both describe how far a complete capture generalizes
and the digest reports them on their own.

*property*dropped_guard_types*: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [int](https://docs.python.org/3/builtins/functions.html#int)]*

The distinct dropped slots counted by guard type.

*property*kept_guard_types*: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [int](https://docs.python.org/3/builtins/functions.html#int)]*

The distinct kept slots counted by guard type.