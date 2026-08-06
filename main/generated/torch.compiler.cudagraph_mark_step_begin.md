# torch.compiler.cudagraph_mark_step_begin

torch.compiler.cudagraph_mark_step_begin()[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/compiler/__init__.py#L505)

Indicates that a new iteration of inference or training is about to begin.

CUDA Graphs will free tensors of a prior iteration. A new iteration is started on each invocation of
torch.compile, so long as there is not a pending backward that has not been called.

If that heuristic is wrong, such as in the following example, manually mark it with this api.

```
@torch.compile(mode="reduce-overhead")
def rand_foo():
 return torch.rand([4], device="cuda")

for _ in range(5):
 torch.compiler.cudagraph_mark_step_begin()
 rand_foo() + rand_foo()
```

For more details, see [torch.compiler_cudagraph_trees](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler_cudagraph_trees.html) # noqa: B950