# torch.func API Reference

## Function Transforms

| [`vmap`](generated/torch.func.vmap.html#torch.func.vmap) | vmap is the vectorizing map; `vmap(func)` returns a new function that maps `func` over some dimension of the inputs. |
| --- | --- |
| [`grad`](generated/torch.func.grad.html#torch.func.grad) | `grad` operator helps computing gradients of `func` with respect to the input(s) specified by `argnums`. |
| [`grad_and_value`](generated/torch.func.grad_and_value.html#torch.func.grad_and_value) | Returns a function to compute a tuple of the gradient and primal, or forward, computation. |
| [`vjp`](generated/torch.func.vjp.html#torch.func.vjp) | Standing for the vector-Jacobian product, returns a tuple containing the results of `func` applied to `primals` and a function that, when given `cotangents`, computes the reverse-mode Jacobian of `func` with respect to `primals` times `cotangents`. |
| [`jvp`](generated/torch.func.jvp.html#torch.func.jvp) | Standing for the Jacobian-vector product, returns a tuple containing the output of func(*primals) and the "Jacobian of `func` evaluated at `primals`" times `tangents`. |
| [`linearize`](generated/torch.func.linearize.html#torch.func.linearize) | Returns the value of `func` at `primals` and linear approximation at `primals`. |
| [`jacrev`](generated/torch.func.jacrev.html#torch.func.jacrev) | Computes the Jacobian of `func` with respect to the arg(s) at index `argnum` using reverse mode autodiff |
| [`jacfwd`](generated/torch.func.jacfwd.html#torch.func.jacfwd) | Computes the Jacobian of `func` with respect to the arg(s) at index `argnum` using forward-mode autodiff |
| [`hessian`](generated/torch.func.hessian.html#torch.func.hessian) | Computes the Hessian of `func` with respect to the arg(s) at index `argnum` via a forward-over-reverse strategy. |
| [`functionalize`](generated/torch.func.functionalize.html#torch.func.functionalize) | functionalize is a transform that can be used to remove (intermediate) mutations and aliasing from a function, while preserving the function's semantics. |

## Utilities for working with torch.nn.Modules

In general, you can transform over a function that calls a `torch.nn.Module`.
For example, the following is an example of computing a jacobian of a function
that takes three values and returns three values:

```
model = torch.nn.Linear(3, 3)

def f(x):
 return model(x)

x = torch.randn(3)
jacobian = jacrev(f)(x)
assert jacobian.shape == (3, 3)
```

However, if you want to do something like compute a jacobian over the parameters of the model, then there needs to be a way to construct a function where the parameters are the inputs to the function. That's what [`functional_call()`](generated/torch.func.functional_call.html#torch.func.functional_call) is for: it accepts an nn.Module, the transformed `parameters`, and the inputs to the Module's forward pass. It returns the value of running the Module's forward pass with the replaced parameters.

Here's how we would compute the Jacobian over the parameters

```
model = torch.nn.Linear(3, 3)

def f(params, x):
 return torch.func.functional_call(model, params, x)

x = torch.randn(3)
jacobian = jacrev(f)(dict(model.named_parameters()), x)
```

| [`functional_call`](generated/torch.func.functional_call.html#torch.func.functional_call) | Performs a functional call on the module by replacing the module parameters and buffers with the provided ones. |
| --- | --- |
| [`stack_module_state`](generated/torch.func.stack_module_state.html#torch.func.stack_module_state) | Prepares a list of torch.nn.Modules for ensembling with [`vmap()`](generated/torch.func.vmap.html#torch.func.vmap). |
| [`replace_all_batch_norm_modules_`](generated/torch.func.replace_all_batch_norm_modules_.html#torch.func.replace_all_batch_norm_modules_) | In place updates `root` by setting the `running_mean` and `running_var` to be None and setting track_running_stats to be False for any nn.BatchNorm module in `root` |

If you're looking for information on fixing Batch Norm modules, please follow the
guidance here

- [Patching Batch Norm](func.batch_norm.html)

## Debug utilities

| [`debug_unwrap`](generated/torch.func.debug_unwrap.html#torch.func.debug_unwrap) | Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor. |
| --- | --- |