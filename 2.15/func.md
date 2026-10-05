# torch.func

torch.func, previously known as "functorch", is
[JAX-like](https://github.com/google/jax) composable function transforms for PyTorch.

Note

This library is currently in [beta](https://pytorch.org/blog/pytorch-feature-classification-changes/#beta).
What this means is that the features generally work (unless otherwise documented)
and we (the PyTorch team) are committed to bringing this library forward. However, the APIs
may change under user feedback and we don't have full coverage over PyTorch operations.

If you have suggestions on the API or use-cases you'd like to be covered, please
open a GitHub issue or reach out. We'd love to hear about how you're using the library.

## What are composable function transforms?

- A "function transform" is a higher-order function that accepts a numerical function
and returns a new function that computes a different quantity.
- [`torch.func`](func.api.html#module-torch.func) has auto-differentiation transforms (`grad(f)` returns a function that
computes the gradient of `f`), a vectorization/batching transform (`vmap(f)`
returns a function that computes `f` over batches of inputs), and others.
- These function transforms can compose with each other arbitrarily. For example,
composing `vmap(grad(f))` computes a quantity called per-sample-gradients that
stock PyTorch cannot efficiently compute today.

## Why composable function transforms?

There are a number of use cases that are tricky to do in PyTorch today:

- computing per-sample-gradients (or other per-sample quantities)
- running ensembles of models on a single machine
- efficiently batching together tasks in the inner-loop of MAML
- efficiently computing Jacobians and Hessians
- efficiently computing batched Jacobians and Hessians

Composing [`vmap()`](generated/torch.func.vmap.html#torch.func.vmap), [`grad()`](generated/torch.func.grad.html#torch.func.grad), and [`vjp()`](generated/torch.func.vjp.html#torch.func.vjp) transforms allows us to express the above without designing a separate subsystem for each.
This idea of composable function transforms comes from the [JAX framework](https://github.com/google/jax).

## Read More

- [torch.func Whirlwind Tour](func.whirlwind_tour.html)

- [What is torch.func?](func.whirlwind_tour.html#what-is-torch-func)
- [Why composable function transforms?](func.whirlwind_tour.html#why-composable-function-transforms)
- [What are the transforms?](func.whirlwind_tour.html#what-are-the-transforms)
- [torch.func API Reference](func.api.html)

- [Function Transforms](func.api.html#function-transforms)
- [Utilities for working with torch.nn.Modules](func.api.html#utilities-for-working-with-torch-nn-modules)
- [Debug utilities](func.api.html#debug-utilities)
- [UX Limitations](func.ux_limitations.html)

- [General limitations](func.ux_limitations.html#general-limitations)
- [torch.autograd APIs](func.ux_limitations.html#torch-autograd-apis)
- [vmap limitations](func.ux_limitations.html#vmap-limitations)
- [Randomness](func.ux_limitations.html#randomness)
- [Migrating from functorch to torch.func](func.migrating.html)

- [function transforms](func.migrating.html#function-transforms)
- [NN module utilities](func.migrating.html#nn-module-utilities)
- [functorch.compile](func.migrating.html#functorch-compile)