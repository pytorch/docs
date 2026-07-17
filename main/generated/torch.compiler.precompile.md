# torch.compiler.precompile

torch.compiler.precompile*= torch.compiler.precompile*

Ahead-of-time precompile `fn` against `example_inputs`.

Note

`torch.compiler.precompile` is NOT
`torch._dynamo.config.caching_precompile` (a `torch.compile` caching
mode); it captures `fn` ahead of time to a self-contained source artifact.

With the default `make_fx` tracer this is a non-strict trace with an explicit
contract; read Note [precompile programming model] before using it. The artifact
faithfully reproduces `fn` only for callers that uphold that contract.

`backend` selects how the captured graph is realized:

- `"eager"` (default): keep the captured ATen graph and run it as-is
(analogous to `torch.compile(backend="eager")`). `python_code` inlines
the readable captured graph (both the inspectable rendering and the executable
artifact); the eager cache carries no compiled artifact (artifact=None) but is
still a full integrity-tagged envelope. The inductor backend is added in a
follow-up.

`tracer` selects the capture front-end:

- `"make_fx"` (default): a NON-STRICT make_fx trace - it records the ATen ops
that actually run when `fn` executes once on the example inputs and does not
analyze your Python, so control flow and shapes are specialized to the example
(the source of the programming-model contract). The only tracer implemented
today.
- `"dynamo"`: planned (a Dynamo-based front-end that analyzes the Python);
raises `NotImplementedError` for now.

`decompositions` is an optional decomposition table (a dict mapping each
`OpOverload` to a decomposition function) forwarded to `make_fx` as its
`decomposition_table` during capture, so you can control how ATen ops are
broken down in the captured graph. Defaults to `None` (make_fx's default).

Returns `(python_code, cache)` - a self-contained, executable Python
source string (the single source of truth for the calling convention) and a
binary cache holding ONLY the backend artifact (NO metadata, NO weights).
Reload a runnable with `torch.compiler.precompile.load(python_code, cache)`.

`fn` is the whole computation, e.g.:

```
python_code, cache = torch.compiler.precompile(
 lambda model, x: model(x), model, x
)

def train_step(model, x, t):
 loss_fn(model(x), t).backward() # or return autograd.grad(...)

python_code, cache = torch.compiler.precompile(train_step, model, x, t)
```

Among `example_inputs`, the `nn.Module` arguments have their params/buffers
lifted to graph inputs (no weights are baked into the artifact - invariant 1);
the rest are the runtime inputs. The reloaded callable is invoked with the SAME
argument structure - pass the model(s) again at runtime, e.g.
`f_c(model, x)`, and that runtime model must match the example model's
parameter/buffer structure (invariant 2). Arguments are matched POSITIONALLY:
pass the model(s) and inputs positionally both here and at load time; keyword-
argument calling conventions are not supported (a fn that relies on them would
surface as a raw arity error). If `fn` ran a backward, the
resulting parameter gradients are scattered (accumulated) onto that runtime
model's `parameters()` `.grad` fields, exactly like eager `.backward()`,
so a `zero_grad()` / `optimizer.step()` loop works unchanged; the artifact
returns `fn`'s own result (`None` for a bare `.backward()` step), not the
grads (invariant 5). Caller responsibilities NOT checked here, and violations
that ARE checked (a baked constant, effectful ops), are in Note [precompile
programming model].

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)]