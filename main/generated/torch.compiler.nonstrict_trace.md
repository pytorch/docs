# torch.compiler.nonstrict_trace

torch.compiler.nonstrict_trace(*traceable_fn*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/compiler/__init__.py#L179)

Decorator to mark a function as nonstrict-traceable for dynamo.

A nonstrict-traced function appears as an opaque call in the dynamo graph.
Dynamo does not trace into the function body (hence the "nonstrict"), but
aot_autograd will trace into it.

This is similar to `allow_in_graph` but with enhanced support for:
- User-defined classes as inputs (must be registered with pytree)
- `nn.Module` as input arguments (parameters and buffers are tracked for autograd)
- Global/captured tensors treated as constants (assumed not updated during execution)

Note

- With `backend="eager"`, the original Python function runs directly.
With `backend="aot_eager"`, the graph traced by aot_autograd runs.
With `backend="inductor"`, the traced graph is compiled with inductor.
- Training is supported: you can call `.backward()` on outputs and gradients
will flow through the nonstrict-traced function.

Dangerous patterns (may cause silent incorrectness):

- Side effects between nonstric_trace'd fn and compiled region: The function should
not depend on variables mutated by other code inside the compiled function, and code
after the call should not depend on mutations made by it.
- Implicit inputs (closures/globals): Tensors captured from enclosing scopes
are treated as constants. Gradients will NOT flow back to them. Pass tensors
as explicit arguments if gradients are needed.

Restrictions:

- Both inputs and outputs must use pytree-compatible types. User-defined classes
must be registered via `torch.utils._pytree.register_pytree_node()`,
`torch.utils._pytree.register_dataclass()`, or
`torch.utils._pytree.register_constant()`. Tensors, Python primitives (int, float, bool, str),
symbolic types (SymInt, SymFloat, SymBool), and built-in containers (list,
tuple, dict) are already handled by default.
- Primitive values and container structure are specialized per call site:
each call site expects the same primitives and structure on every execution.

Example:

```
>>> import torch
>>> @torch.compiler.nonstrict_trace
... def traced_forward(model, x):
... # It's OK to have dynamo graph break within nonstrict_trace region
... torch._dynamo.graph_break()
... return model(x) + x
...
>>> class MyModule(torch.nn.Module):
... def __init__(self):
... super().__init__()
... self.inner = torch.nn.Linear(10, 10)
...
... def forward(self, x):
... return traced_forward(self.inner, x)
...
>>> # Compile and run
>>> model = MyModule()
>>> opt_model = torch.compile(model, backend="aot_eager", fullgraph=True)
>>> out = opt_model(torch.randn(10, 10))
>>> out.sum().backward() # Gradients flow through traced_forward
```

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]