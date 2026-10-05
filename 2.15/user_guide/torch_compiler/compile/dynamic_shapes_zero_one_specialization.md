# The Zero-One Specialization Problem

Before you read this section, you should understand the basics of
dynamic shapes. Make sure you have read the following sections:

- [Dynamic Shapes](../torch.compiler_dynamic_shapes.html#dynamic-shapes)
- [torch.export](../export.html#torch-export)
- [What is a specialization?](../torch.compiler_dynamic_shapes.html#what-is-a-specialization)

In `torch.compile`, we specialize automatically on inputs with sizes
0 or 1 and assume that any remaining inputs cannot be 0 or 1. This
simplifies tasks like contiguity and broadcasting checks, as it
avoids adding extra guards. However, this can cause problems for
sparse models with many symbolic integers that in practice have
tensors of size 0, 1, or 2. For example, consider when you a task is
something like collecting likes on page.

While it's possible to stop specializing on 0/1 upfront, executing
normal PyTorch code often reintroduces 0/1 guards, as many conditions
in PyTorch check for values being 0 or 1. Although models that work
for `N > 2` often generalize to `N = 1`, this isn't guaranteed, especially
with symbolic variables. For example, in hand tracking, a dimension
size of `N = 0`, `1`, or `2` may lead to different graph behaviors.
Simply hoping that the `N > 2` model generalizes can expose soundness issues.

See also

- [Dynamic Shapes](../torch.compiler_dynamic_shapes.html#dynamic-shapes)
- [torch.export](../export.html#torch-export)
- [What is a specialization?](../torch.compiler_dynamic_shapes.html#what-is-a-specialization)
- [Backed vs Unbacked Symints](dynamic_shapes_backed_unbacked.html#backed-vs-unbacked-symints)