# torch.fx.passes.runtime_assert.insert_deferred_runtime_asserts

torch.fx.passes.runtime_assert.insert_deferred_runtime_asserts(*gm*, *shape_env*, *name*, *export=False*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/fx/passes/runtime_assert.py#L54)

During tracing, we may have discovered that some data-dependent values
had runtime assert on them; e.g., torch.empty(x.item()) induces a runtime
that x.item() >= 0. These asserts can happen unpredictably during fake
tensor propagation, so we cannot conveniently insert them into the FX graph
when they occur. Instead, we accumulate them in the ShapeEnv, and in this
pass insert them into the graph as proper tests.

This pass also deduplicates size-related computation, CSE-ing ops that produce
symbolic values and/or are involved in runtime asserts. Additionally, shape calls
(size/stride/storage_offset) are turned into compute on input sizes if possible,
allowing intermediate tensors to be freed earlier. For example, here dynamo will
DCE the cat and repeat calls:

> z = torch.cat([x, x], dim=0) # 2*s0
> w = z.repeat(y.shape[0]) # 2*s0*s1
> _w = w.shape[0]
> # something with _w, but not w ...
> 
> 
> 
> 
> # turns into ->
> _w0 = 2 * s0
> _w = _w0 * s1
> 
> 
> 
> 
> # where s0, s1 are either SymInt graph inputs, or the result of added size calls

Redundant compiler-generated asserts that assert the same expression, and
redundant constrain_range calls are also deduplicated. Additionally, because
single-symbol bound checks (e.g. u0 >= 0, u0 <= 5) accumulate information in
the ShapeEnv, the ShapeEnv contains min/max bounds for each symbol, and we
add bound checks at the end of this pass when an equivalent explicit assert
is not already present in the graph.

Note

Backwards-compatibility for this API is guaranteed.