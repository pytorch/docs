# Automatic differentiation package - torch.autograd

`torch.autograd` provides classes and functions implementing automatic differentiation of arbitrary scalar valued functions.

It requires minimal changes to the existing code - you only need to declare `Tensor` s
for which gradients should be computed with the `requires_grad=True` keyword.
As of now, we only support autograd for floating point `Tensor` types (
half, float, double and bfloat16) and complex `Tensor` types (cfloat, cdouble).

| [`backward`](generated/torch.autograd.backward.html#torch.autograd.backward) | Compute the sum of gradients of given tensors with respect to graph leaves. |
| --- | --- |
| [`grad`](generated/torch.autograd.grad.html#torch.autograd.grad) | Compute and return the sum of gradients of outputs with respect to the inputs. |

## Forward-mode Automatic Differentiation

Warning

This API is in beta. Even though the function signatures are very unlikely to change, improved
operator coverage is planned before we consider this stable.

Please see the [forward-mode AD tutorial](https://pytorch.org/tutorials/intermediate/forward_ad_usage.html)
for detailed steps on how to use this API.

| [`forward_ad.dual_level`](generated/torch.autograd.forward_ad.dual_level.html#torch.autograd.forward_ad.dual_level) | Context-manager for forward AD, where all forward AD computation must occur within the `dual_level` context. |
| --- | --- |
| [`forward_ad.make_dual`](generated/torch.autograd.forward_ad.make_dual.html#torch.autograd.forward_ad.make_dual) | Associate a tensor value with its tangent to create a "dual tensor" for forward AD gradient computation. |
| [`forward_ad.unpack_dual`](generated/torch.autograd.forward_ad.unpack_dual.html#torch.autograd.forward_ad.unpack_dual) | Unpack a "dual tensor" to get both its Tensor value and its forward AD gradient. |
| [`forward_ad.enter_dual_level`](generated/torch.autograd.forward_ad.enter_dual_level.html#torch.autograd.forward_ad.enter_dual_level) | Enter a new forward grad level. |
| [`forward_ad.exit_dual_level`](generated/torch.autograd.forward_ad.exit_dual_level.html#torch.autograd.forward_ad.exit_dual_level) | Exit a forward grad level. |
| [`forward_ad.UnpackedDualTensor`](generated/torch.autograd.forward_ad.UnpackedDualTensor.html#torch.autograd.forward_ad.UnpackedDualTensor) | Namedtuple returned by `unpack_dual()` containing the primal and tangent components of the dual tensor. |

## Functional higher level API

Warning

This API is in beta. Even though the function signatures are very unlikely to change, major
improvements to performances are planned before we consider this stable.

This section contains the higher level API for the autograd that builds on the basic API above
and allows you to compute jacobians, hessians, etc.

This API works with user-provided functions that take only Tensors as input and return
only Tensors.
If your function takes other arguments that are not Tensors or Tensors that don't have requires_grad set,
you can use a lambda to capture them.
For example, for a function `f` that takes three inputs, a Tensor for which we want the jacobian, another
tensor that should be considered constant and a boolean flag as `f(input, constant, flag=flag)`
you can use it as `functional.jacobian(lambda x: f(x, constant, flag=flag), input)`.

| [`functional.jacobian`](generated/torch.autograd.functional.jacobian.html#torch.autograd.functional.jacobian) | Compute the Jacobian of a given function. |
| --- | --- |
| [`functional.hessian`](generated/torch.autograd.functional.hessian.html#torch.autograd.functional.hessian) | Compute the Hessian of a given scalar function. |
| [`functional.vjp`](generated/torch.autograd.functional.vjp.html#torch.autograd.functional.vjp) | Compute the dot product between a vector `v` and the Jacobian of the given function at the point given by the inputs. |
| [`functional.jvp`](generated/torch.autograd.functional.jvp.html#torch.autograd.functional.jvp) | Compute the dot product between the Jacobian of the given function at the point given by the inputs and a vector `v`. |
| [`functional.vhp`](generated/torch.autograd.functional.vhp.html#torch.autograd.functional.vhp) | Compute the dot product between vector `v` and Hessian of a given scalar function at a specified point. |
| [`functional.hvp`](generated/torch.autograd.functional.hvp.html#torch.autograd.functional.hvp) | Compute the dot product between the scalar function's Hessian and a vector `v` at a specified point. |

## Locally disabling gradient computation

See [Locally disabling gradient computation](notes/autograd.html#locally-disable-grad-doc) for more information on the differences
between no-grad and inference mode as well as other related mechanisms that
may be confused with the two. Also see [Locally disabling gradient computation](torch.html#torch-rst-local-disable-grad)
for a list of functions that can be used to locally disable gradients.

## Default gradient layouts

When a non-sparse `param` receives a non-sparse gradient during
[`torch.autograd.backward()`](generated/torch.autograd.backward.html#torch.autograd.backward) or [`torch.Tensor.backward()`](generated/torch.Tensor.backward.html#torch.Tensor.backward)
`param.grad` is accumulated as follows.

If `param.grad` is initially `None`:

1. If `param`'s memory is non-overlapping and dense, `.grad` is
created with strides matching `param` (thus matching `param`'s
layout).
2. Otherwise, `.grad` is created with rowmajor-contiguous strides.

If `param` already has a non-sparse `.grad` attribute:

1. If `create_graph=False`, `backward()` accumulates into `.grad`
in-place, which preserves its strides.
2. If `create_graph=True`, `backward()` replaces `.grad` with a
new tensor `.grad + new grad`, which attempts (but does not guarantee)
matching the preexisting `.grad`'s strides.

The default behavior (letting `.grad`s be `None` before the first
`backward()`, such that their layout is created according to 1 or 2,
and retained over time according to 3 or 4) is recommended for best performance.
Calls to `model.zero_grad()` or `optimizer.zero_grad()` will not affect `.grad`
layouts.

In fact, resetting all `.grad`s to `None` before each
accumulation phase, e.g.:

```
for iterations...
 ...
 for param in model.parameters():
 param.grad = None
 loss.backward()
```

such that they're recreated according to 1 or 2 every time,
is a valid alternative to `model.zero_grad()` or `optimizer.zero_grad()`
that may improve performance for some networks.

### Manual gradient layouts

If you need manual control over `.grad`'s strides,
assign `param.grad =` a zeroed tensor with desired strides
before the first `backward()`, and never reset it to `None`.
3 guarantees your layout is preserved as long as `create_graph=False`.
4 indicates your layout is *likely* preserved even if `create_graph=True`.

## In-place operations on Tensors

Supporting in-place operations in autograd is a hard matter, and we discourage
their use in most cases. Autograd's aggressive buffer freeing and reuse makes
it very efficient and there are very few occasions when in-place operations
actually lower memory usage by any significant amount. Unless you're operating
under heavy memory pressure, you might never need to use them.

### In-place correctness checks

All `Tensor` s keep track of in-place operations applied to them, and
if the implementation detects that a tensor was saved for backward in one of
the functions, but it was modified in-place afterwards, an error will be raised
once backward pass is started. This ensures that if you're using in-place
functions and not seeing any errors, you can be sure that the computed
gradients are correct.

## Variable (deprecated)

Warning

The Variable API has been deprecated: Variables are no longer necessary to
use autograd with tensors. Autograd automatically supports Tensors with
`requires_grad` set to `True`. Below please find a quick guide on what
has changed:

- `Variable(tensor)` and `Variable(tensor, requires_grad)` still work as expected,
but they return Tensors instead of Variables.
- `var.data` is the same thing as `tensor.data`.
- Methods such as `var.backward(), var.detach(), var.register_hook()` now work on tensors
with the same method names.

In addition, one can now create tensors with `requires_grad=True` using factory
methods such as [`torch.randn()`](generated/torch.randn.html#torch.randn), [`torch.zeros()`](generated/torch.zeros.html#torch.zeros), [`torch.ones()`](generated/torch.ones.html#torch.ones), and others
like the following:

`autograd_tensor = torch.randn((2, 3, 4), requires_grad=True)`

## Tensor autograd functions

| `torch.Tensor.grad` | This attribute is `None` by default and becomes a Tensor the first time a call to [`backward()`](generated/torch.autograd.backward.html#torch.autograd.backward) computes gradients for `self`. |
| --- | --- |
| `torch.Tensor.requires_grad` | Is `True` if gradients need to be computed for this Tensor, `False` otherwise. |
| `torch.Tensor.is_leaf` | All Tensors that have `requires_grad` which is `False` will be leaf Tensors by convention. |
| `torch.Tensor.backward`([gradient, ...]) | Computes the gradient of current tensor wrt graph leaves. |
| `torch.Tensor.detach` | Returns a new Tensor, detached from the current graph. |
| `torch.Tensor.detach_` | Detaches the Tensor from the graph that created it, making it a leaf. |
| `torch.Tensor.register_hook`(hook) | Registers a backward hook. |
| `torch.Tensor.register_post_accumulate_grad_hook`(hook) | Registers a backward hook that runs after grad accumulation. |
| `torch.Tensor.retain_grad`() | Enables this Tensor to have their [`grad`](generated/torch.autograd.grad.html#torch.autograd.grad) populated during [`backward()`](generated/torch.autograd.backward.html#torch.autograd.backward). |

## Function

*class*torch.autograd.Function(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/function.py#L555)

Base class to create custom autograd.Function.

To create a custom autograd.Function, subclass this class and implement
the [`forward()`](generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward) and [`backward()`](generated/torch.autograd.backward.html#torch.autograd.backward) static methods. Then, to use your custom
op in the forward pass, call the class method `apply`. Do not call
[`forward()`](generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward) directly.

To ensure correctness and best performance, make sure you are calling the
correct methods on `ctx` and validating your backward function using
`torch.autograd.gradcheck()`.

See [Extending torch.autograd](notes/extending.html#extending-autograd) for more details on how to use this class.

Examples:

```
>>> class Exp(Function):
>>> @staticmethod
>>> def forward(ctx, i):
>>> result = i.exp()
>>> ctx.save_for_backward(result)
>>> return result
>>>
>>> @staticmethod
>>> def backward(ctx, grad_output):
>>> result, = ctx.saved_tensors
>>> return grad_output * result
>>>
>>> # Use it by calling the apply method:
>>> output = Exp.apply(input)
```

| [`Function.forward`](generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward) | Define the forward of the custom autograd Function. |
| --- | --- |
| [`Function.backward`](generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward) | Define a formula for differentiating the operation with backward mode automatic differentiation. |
| [`Function.jvp`](generated/torch.autograd.Function.jvp.html#torch.autograd.Function.jvp) | Define a formula for differentiating the operation with forward mode automatic differentiation. |
| [`Function.vmap`](generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap) | Define the behavior for this autograd.Function underneath [`torch.vmap()`](generated/torch.vmap.html#torch.vmap). |

## Context method mixins

When creating a new `Function`, the following methods are available to `ctx`.

*class*torch.autograd.function.FunctionCtx[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/function.py#L38)

*class*torch.autograd.function.FunctionMeta(*name*, *bases*, *attrs*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/function.py#L387)

Function metaclass.

This metaclass sets up the following properties:
_backward_cls: The Function class corresponding to the differentiated

version of this function (which is generated on the fly by this
metaclass).

| [`function.FunctionCtx.mark_dirty`](generated/torch.autograd.function.FunctionCtx.mark_dirty.html#torch.autograd.function.FunctionCtx.mark_dirty) | Mark given tensors as modified in an in-place operation. |
| --- | --- |
| [`function.FunctionCtx.mark_non_differentiable`](generated/torch.autograd.function.FunctionCtx.mark_non_differentiable.html#torch.autograd.function.FunctionCtx.mark_non_differentiable) | Mark outputs as non-differentiable. |
| [`function.FunctionCtx.save_for_backward`](generated/torch.autograd.function.FunctionCtx.save_for_backward.html#torch.autograd.function.FunctionCtx.save_for_backward) | Save given tensors for a future call to [`backward()`](generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward). |
| [`function.FunctionCtx.set_materialize_grads`](generated/torch.autograd.function.FunctionCtx.set_materialize_grads.html#torch.autograd.function.FunctionCtx.set_materialize_grads) | Set whether to materialize grad tensors. |

## Custom Function utilities

Decorator for backward method.

| [`function.once_differentiable`](generated/torch.autograd.function.once_differentiable.html#torch.autograd.function.once_differentiable) | |
| --- | --- |

Base custom `Function` used to build PyTorch utilities

| [`function.BackwardCFunction`](generated/torch.autograd.function.BackwardCFunction.html#torch.autograd.function.BackwardCFunction) | This class is used for internal autograd work. |
| --- | --- |
| [`function.InplaceFunction`](generated/torch.autograd.function.InplaceFunction.html#torch.autograd.function.InplaceFunction) | This class is here only for backward compatibility reasons. |
| [`function.NestedIOFunction`](generated/torch.autograd.function.NestedIOFunction.html#torch.autograd.function.NestedIOFunction) | This class is here only for backward compatibility reasons. |

## Numerical gradient checking

| [`gradcheck`](generated/torch.autograd.gradcheck.gradcheck.html#torch.autograd.gradcheck.gradcheck) | Check gradients computed via small finite differences against analytical gradients wrt tensors in `inputs` that are of floating point or complex type and with `requires_grad=True`. |
| --- | --- |
| [`gradgradcheck`](generated/torch.autograd.gradcheck.gradgradcheck.html#torch.autograd.gradcheck.gradgradcheck) | Check gradients of gradients computed via small finite differences against analytical gradients wrt tensors in `inputs` and `grad_outputs` that are of floating point or complex type and with `requires_grad=True`. |
| [`GradcheckError`](generated/torch.autograd.gradcheck.GradcheckError.html#torch.autograd.gradcheck.GradcheckError) | Error raised by [`gradcheck()`](generated/torch.autograd.gradcheck.gradcheck.html#torch.autograd.gradcheck.gradcheck) and [`gradgradcheck()`](generated/torch.autograd.gradcheck.gradgradcheck.html#torch.autograd.gradcheck.gradgradcheck). |
| [`get_analytical_jacobian`](generated/torch.autograd.gradcheck.get_analytical_jacobian.html#torch.autograd.gradcheck.get_analytical_jacobian) | |
| [`get_numerical_jacobian`](generated/torch.autograd.gradcheck.get_numerical_jacobian.html#torch.autograd.gradcheck.get_numerical_jacobian) | Compute the numerical Jacobian for a given fn and its inputs. |
| [`get_numerical_jacobian_wrt_specific_input`](generated/torch.autograd.gradcheck.get_numerical_jacobian_wrt_specific_input.html#torch.autograd.gradcheck.get_numerical_jacobian_wrt_specific_input) | |

## Profiler

Autograd includes a profiler that lets you inspect the cost of different
operators inside your model - both on the CPU and GPU. There are three modes
implemented at the moment - CPU-only using `profile`.
nvprof based (registers both CPU and GPU activity) using
`emit_nvtx`.
and vtune profiler based using
`emit_itt`.

*class*torch.autograd.profiler.profile(*enabled=True*, ***, *use_device=None*, *record_shapes=False*, *with_flops=False*, *profile_memory=False*, *with_stack=False*, *with_modules=False*, *use_kineto=False*, *use_cpu=True*, *experimental_config=None*, *acc_events=False*, *custom_trace_id_callback=None*, *post_processing_timeout_s=None*, *activity_filters=None*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/profiler.py#L113)

Context manager that manages autograd profiler state and holds a summary of results.

Note

This is the backend, most people should use [`torch.profiler`](profiler.html#module-torch.profiler) instead.

Under the hood it just records events of functions being executed in C++ and
exposes those events to Python. You can wrap any code into it and it will
only report runtime of PyTorch functions.
Note: profiler is thread local and is automatically propagated into the async tasks

Parameters:

- **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Setting this to False makes this context manager a no-op.
- **use_device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Enables timing of device events.
Adds approximately 4us of overhead to each tensor operation when use cuda.
The valid devices options are 'cuda', 'xpu', 'mtia' and 'privateuseone'.
- **record_shapes** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If shapes recording is set, information
about input dimensions will be collected. This allows one to see which
dimensions have been used under the hood and further group by them
using prof.key_averages(group_by_input_shape=True). Please note that
shape recording might skew your profiling data. It is recommended to
use separate runs with and without shape recording to validate the timing.
Most likely the skew will be negligible for bottom most events (in a case
of nested function calls). But for higher level functions the total
self cpu time might be artificially increased because of the shape
collection.
- **with_flops** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If with_flops is set, the profiler will estimate
the FLOPs (floating point operations) value using the operator's input shape.
This allows one to estimate the hardware performance. Currently,
this option only works for the matrix multiplication and 2D convolution operators.
- **profile_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - track tensor memory allocation/deallocation.
- **with_stack** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - record source information (file and line number) for the ops.
- **with_modules** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) -

record module hierarchy (including function names)
corresponding to the callstack of the op. e.g. If module A's forward call's
module B's forward which contains an aten::add op,
then aten::add's module hierarchy is A.B

Deprecated since version ``with_modules``: is deprecated and will be removed in a future version.
It only collects data for TorchScript models, which are themselves
deprecated, and does nothing in eager mode. Use `with_stack=True`,
which records `nn.Module` events for eager models.
- **use_kineto** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - experimental, enable profiling with Kineto profiler.
- **use_cpu** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - profile CPU events; setting to `False` requires
`use_kineto=True` and can be used to lower the overhead for GPU-only profiling.
- **experimental_config** (*_ExperimentalConfig*) - A set of experimental options
used by profiler libraries like Kineto. Note, backward compatibility is not guaranteed.
- **acc_events** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Enable the accumulation of FunctionEvents across multiple profiling cycles
- **post_processing_timeout_s** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Optional timeout in seconds for post-processing profiler
results. In this context, post-processing happens after the profiling itself has finished.
If specified, event parsing will stop after this duration and return partial results. Useful
for handling large traces that may take too long to process.

Warning

Enabling memory profiling or source attribution incurs additional profiler
overhead

Warning

This context managers should not be called recursively, i.e. no nested
instances are allowed

Warning

Due to some CUDA multiprocessing limitations (see [CUDA in multiprocessing](notes/multiprocessing.html#multiprocessing-cuda-note)),
one cannot use the profiler with `use_device = 'cuda'` to benchmark
DataLoaders with `num_workers > 0`. If you wish to benchmark data loading,
please use `use_device = None` or `num_workers = 0`.

Example

```
>>> x = torch.randn((1, 1), requires_grad=True)
>>> with torch.autograd.profiler.profile() as prof:
>>> for _ in range(100): # any normal python code, really!
>>> y = x ** 2
>>> y.backward()
>>> # NOTE: some columns were removed for brevity
>>> print(prof.key_averages().table(sort_by="self_cpu_time_total"))
----------------------------------- --------------- --------------- ---------------
Name Self CPU total CPU time avg Number of Calls
----------------------------------- --------------- --------------- ---------------
mul 32.048ms 32.048ms 200
pow 27.041ms 27.041ms 200
PowBackward0 9.727ms 55.483ms 100
torch::autograd::AccumulateGrad 9.148ms 9.148ms 100
torch::autograd::GraphRoot 691.816us 691.816us 100
----------------------------------- --------------- --------------- ---------------
```

| [`profiler.profile.export_chrome_trace`](generated/torch.autograd.profiler.profile.export_chrome_trace.html#torch.autograd.profiler.profile.export_chrome_trace) | Export an EventList as a Chrome tracing tools file. |
| --- | --- |
| [`profiler.profile.key_averages`](generated/torch.autograd.profiler.profile.key_averages.html#torch.autograd.profiler.profile.key_averages) | Averages all function events over their keys. |
| [`profiler.profile.self_cpu_time_total`](generated/torch.autograd.profiler.profile.self_cpu_time_total.html#torch.autograd.profiler.profile.self_cpu_time_total) | Returns total time spent on CPU. |
| [`profiler.profile.total_average`](generated/torch.autograd.profiler.profile.total_average.html#torch.autograd.profiler.profile.total_average) | Compute aggregate statistics across all events. |
| [`profiler.parse_nvprof_trace`](generated/torch.autograd.profiler.parse_nvprof_trace.html#torch.autograd.profiler.parse_nvprof_trace) | |
| [`profiler.EnforceUnique`](generated/torch.autograd.profiler.EnforceUnique.html#torch.autograd.profiler.EnforceUnique) | Raises an error if a key is seen more than once. |
| [`profiler.KinetoStepTracker`](generated/torch.autograd.profiler.KinetoStepTracker.html#torch.autograd.profiler.KinetoStepTracker) | Provides an abstraction for incrementing the step count globally. |
| [`profiler.record_function`](generated/torch.autograd.profiler.record_function.html#torch.autograd.profiler.record_function) | Context manager/function decorator that adds a label to a code block/function when running autograd profiler. |
| [`profiler_util.EventList`](generated/torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList) | A list of profiling events with helper methods for analysis and visualization. |
| [`profiler_util.FormattedTimesMixin`](generated/torch.autograd.profiler_util.FormattedTimesMixin.html#torch.autograd.profiler_util.FormattedTimesMixin) | Helpers for FunctionEvent and FunctionEventAvg. |
| [`profiler_util.FunctionEvent`](generated/torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent) | Profiling information about a single function. |
| [`profiler_util.FunctionEventAvg`](generated/torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg) | Averaged profiling statistics over multiple FunctionEvent objects. |
| [`profiler_util.Interval`](generated/torch.autograd.profiler_util.Interval.html#torch.autograd.profiler_util.Interval) | |
| [`profiler_util.Kernel`](generated/torch.autograd.profiler_util.Kernel.html#torch.autograd.profiler_util.Kernel) | |
| [`profiler_util.MemRecordsAcc`](generated/torch.autograd.profiler_util.MemRecordsAcc.html#torch.autograd.profiler_util.MemRecordsAcc) | Acceleration structure for accessing mem_records in interval. |
| [`profiler_util.StringTable`](generated/torch.autograd.profiler_util.StringTable.html#torch.autograd.profiler_util.StringTable) | |

*class*torch.autograd.profiler.emit_nvtx(*enabled=True*, *record_shapes=False*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/profiler.py#L1079)

Context manager that makes every autograd operation emit an NVTX range.

It is useful when running the program under nvprof:

```
nvprof --profile-from-start off -o trace_name.prof -- <regular command here>
```

Unfortunately, there's no way to force nvprof to flush the data it collected
to disk, so for CUDA profiling one has to use this context manager to annotate
nvprof traces and wait for the process to exit before inspecting them.
Then, either NVIDIA Visual Profiler (nvvp) can be used to visualize the timeline, or
[`torch.autograd.profiler.load_nvprof()`](generated/torch.autograd.profiler.load_nvprof.html#torch.autograd.profiler.load_nvprof) can load the results for inspection
e.g. in Python REPL.

Parameters:

- **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Setting `enabled=False` makes this context manager a no-op.
Default: `True`.
- **record_shapes** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `record_shapes=True`, the nvtx range wrapping
each autograd op will append information about the sizes of Tensor arguments received
by that op, in the following format:
`[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]`
Non-tensor arguments will be represented by `[]`.
Arguments will be listed in the order they are received by the backend op.
Please note that this order may not match the order in which those arguments were passed
on the Python side. Also note that shape recording may increase the overhead of nvtx range creation.
Default: `False`

Example

```
>>> with torch.cuda.profiler.profile():
... model(x) # Warmup CUDA memory allocator and profiler
... with torch.autograd.profiler.emit_nvtx():
... model(x)
```

**Forward-backward correlation**

When viewing a profile created using `emit_nvtx` in the Nvidia Visual Profiler,
correlating each backward-pass op with the corresponding forward-pass op can be difficult.
To ease this task, `emit_nvtx` appends sequence number information to the ranges it
generates.

During the forward pass, each function range is decorated with `seq=<N>`. `seq` is a running
counter, incremented each time a new backward Function object is created and stashed for backward.
Thus, the `seq=<N>` annotation associated with each forward function range tells you that
if a backward Function object is created by this forward function,
the backward object will receive sequence number N.
During the backward pass, the top-level range wrapping each C++ backward Function's
`apply()` call is decorated with `stashed seq=<M>`. `M` is the sequence number that
the backward object was created with. By comparing `stashed seq` numbers in backward with `seq`
numbers in forward, you can track down which forward op created each backward Function.

Any functions executed during the backward pass are also decorated with `seq=<N>`. During
default backward (with `create_graph=False`) this information is irrelevant, and in fact,
`N` may simply be 0 for all such functions. Only the top-level ranges associated with
backward Function objects' `apply()` methods are useful, as a way to correlate these Function
objects with the earlier forward pass.

**Double-backward**

If, on the other hand, a backward pass with `create_graph=True` is underway (in other words,
if you are setting up for a double-backward), each function's execution during backward
is given a nonzero, useful `seq=<N>`. Those functions may themselves create Function objects
to be executed later during double-backward, just as the original functions in the forward pass did.
The relationship between backward and double-backward is conceptually the same as the relationship
between forward and backward: The functions still emit current-sequence-number-tagged ranges,
the Function objects they create still stash those sequence numbers, and during the eventual
double-backward, the Function objects' `apply()` ranges are still tagged with `stashed seq`
numbers, which can be compared to seq numbers from the backward pass.

*class*torch.autograd.profiler.emit_itt(*enabled=True*, *record_shapes=False*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/profiler.py#L1008)

Context manager that makes every autograd operation emit an ITT range.

It is useful when running the program under Intel(R) VTune Profiler:

```
vtune <--vtune-flags> <regular command here>
```

The Instrumentation and Tracing Technology (ITT) API enables your application to generate and
control the collection of trace data during its execution across different Intel tools.
This context manager is to annotate Intel(R) VTune Profiling trace. With help of this context manager,
you will be able to see labeled ranges in Intel(R) VTune Profiler GUI.

Parameters:

- **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Setting `enabled=False` makes this context manager a no-op.
Default: `True`.
- **record_shapes** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `record_shapes=True`, the itt range wrapping
each autograd op will append information about the sizes of Tensor arguments received
by that op, in the following format:
`[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]`
Non-tensor arguments will be represented by `[]`.
Arguments will be listed in the order they are received by the backend op.
Please note that this order may not match the order in which those arguments were passed
on the Python side. Also note that shape recording may increase the overhead of itt range creation.
Default: `False`

Example

```
>>> with torch.autograd.profiler.emit_itt():
... model(x)
```

| [`profiler.load_nvprof`](generated/torch.autograd.profiler.load_nvprof.html#torch.autograd.profiler.load_nvprof) | Open an nvprof trace file and parses autograd annotations. |
| --- | --- |

## Debugging and anomaly detection

*class*torch.autograd.detect_anomaly(*check_nan=True*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/anomaly_mode.py#L12)

Context-manager that enables anomaly detection for the autograd engine.

This does two things:

- Running the forward pass with detection enabled will allow the backward
pass to print the traceback of the forward operation that created the failing
backward function.
- If `check_nan` is `True`, any backward computation that generates "nan"
value will raise an error. Default `True`.

Warning

This mode should be enabled only for debugging as the different tests
will slow down your program execution.

Example

```
>>> import torch
>>> from torch import autograd
>>> class MyFunc(autograd.Function):
... @staticmethod
... def forward(ctx, inp):
... return inp.clone()
...
... @staticmethod
... def backward(ctx, gO):
... # Error during the backward pass
... raise RuntimeError("Some error in backward")
... return gO.clone()
>>> def run_fn(a):
... out = MyFunc.apply(a)
... return out.sum()
>>> inp = torch.rand(10, 10, requires_grad=True)
>>> out = run_fn(inp)
>>> out.backward()
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/your/pytorch/install/torch/_tensor.py", line 93, in backward
 torch.autograd.backward(self, gradient, retain_graph, create_graph)
 File "/your/pytorch/install/torch/autograd/__init__.py", line 90, in backward
 allow_unreachable=True) # allow_unreachable flag
 File "/your/pytorch/install/torch/autograd/function.py", line 76, in apply
 return self._forward_cls.backward(self, *args)
 File "<stdin>", line 8, in backward
 RuntimeError: Some error in backward
>>> with autograd.detect_anomaly():
... inp = torch.rand(10, 10, requires_grad=True)
... out = run_fn(inp)
... out.backward()
 Traceback of forward call that caused the error:
 File "tmp.py", line 53, in <module>
 out = run_fn(inp)
 File "tmp.py", line 44, in run_fn
 out = MyFunc.apply(a)
 Traceback (most recent call last):
 File "<stdin>", line 4, in <module>
 File "/your/pytorch/install/torch/_tensor.py", line 93, in backward
 torch.autograd.backward(self, gradient, retain_graph, create_graph)
 File "/your/pytorch/install/torch/autograd/__init__.py", line 90, in backward
 allow_unreachable=True) # allow_unreachable flag
 File "/your/pytorch/install/torch/autograd/function.py", line 76, in apply
 return self._forward_cls.backward(self, *args)
 File "<stdin>", line 8, in backward
 RuntimeError: Some error in backward
```

*class*torch.autograd.set_detect_anomaly(*mode*, *check_nan=True*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/anomaly_mode.py#L97)

Context-manager that sets the anomaly detection for the autograd engine on or off.

`set_detect_anomaly` will enable or disable the autograd anomaly detection
based on its argument `mode`.
It can be used as a context-manager or as a function.

See `detect_anomaly` above for details of the anomaly detection behaviour.

Parameters:

- **mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Flag whether to enable anomaly detection (`True`),
or disable (`False`).
- **check_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Flag whether to raise an error when the backward
generate "nan"

| [`grad_mode.set_multithreading_enabled`](generated/torch.autograd.grad_mode.set_multithreading_enabled.html#torch.autograd.grad_mode.set_multithreading_enabled) | Context-manager that enables or disables multithreaded backward. |
| --- | --- |
| [`grad_mode.enforce_grad_layout_policy`](generated/torch.autograd.grad_mode.enforce_grad_layout_policy.html#torch.autograd.grad_mode.enforce_grad_layout_policy) | Context-manager that controls the gradient layout policy enforcement. |

## Autograd graph

Autograd exposes methods that allow one to inspect the graph and interpose behavior during
the backward pass.

The `grad_fn` attribute of a [`torch.Tensor`](tensors.html#torch.Tensor) holds a `torch.autograd.graph.Node`
if the tensor is the output of a operation that was recorded by autograd (i.e., grad_mode is
enabled and at least one of the inputs required gradients), or `None` otherwise.

| [`graph.Node.name`](generated/torch.autograd.graph.Node.name.html#torch.autograd.graph.Node.name) | Return the name. |
| --- | --- |
| [`graph.Node.metadata`](generated/torch.autograd.graph.Node.metadata.html#torch.autograd.graph.Node.metadata) | Return the metadata. |
| [`graph.Node.next_functions`](generated/torch.autograd.graph.Node.next_functions.html#torch.autograd.graph.Node.next_functions) | Return the edges from this node to its input functions. |
| [`graph.Node.register_hook`](generated/torch.autograd.graph.Node.register_hook.html#torch.autograd.graph.Node.register_hook) | Register a backward hook. |
| [`graph.Node.register_prehook`](generated/torch.autograd.graph.Node.register_prehook.html#torch.autograd.graph.Node.register_prehook) | Register a backward pre-hook. |
| [`graph.increment_version`](generated/torch.autograd.graph.increment_version.html#torch.autograd.graph.increment_version) | Update autograd metadata tracking whether the given Tensor was modified in place. |

Some operations need intermediary results to be saved during the forward pass
in order to execute the backward pass.
These intermediary results are saved as attributes on the `grad_fn` and can be accessed.
For example:

```
>>> a = torch.tensor([0., 0., 0.], requires_grad=True)
>>> b = a.exp()
>>> print(isinstance(b.grad_fn, torch.autograd.graph.Node))
True
>>> print(dir(b.grad_fn))
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_raw_saved_result', '_register_hook_dict', '_saved_result', 'metadata', 'name', 'next_functions', 'register_hook', 'register_prehook', 'requires_grad']
>>> print(torch.allclose(b.grad_fn._saved_result, b))
True
```

You can also define how these saved tensors should be packed / unpacked using hooks.
A common application is to trade compute for memory by saving those intermediary results
to disk or to CPU instead of leaving them on the GPU. This is especially useful if you
notice your model fits on GPU during evaluation, but not training.
When writing a `pack_hook` that keeps its input tensor, call `.detach()` on it first
to avoid a reference cycle when the saved tensor is a graph output; see
[Hooks for saved tensors](notes/autograd.html#saved-tensors-hooks-doc) for details.

*class*torch.autograd.graph.saved_tensors_hooks(*pack_hook*, *unpack_hook*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L273)

Context-manager that sets a pair of pack / unpack hooks for saved tensors.

Use this context-manager to define how intermediary results of an operation
should be packed before saving, and unpacked on retrieval.

In that context, the `pack_hook` function will be called every time an
operation saves a tensor for backward (this includes intermediary results
saved using
`save_for_backward()` but
also those recorded by a PyTorch-defined operation). The output of
`pack_hook` is then stored in the computation graph instead of the
original tensor.

The `unpack_hook` is called when the saved tensor needs to be accessed,
namely when executing [`torch.Tensor.backward()`](generated/torch.Tensor.backward.html#torch.Tensor.backward) or
[`torch.autograd.grad()`](generated/torch.autograd.grad.html#torch.autograd.grad). It takes as argument the *packed* object
returned by `pack_hook` and should return a tensor which has the same
content as the original tensor (passed as input to the corresponding
`pack_hook`).

The hooks should have the following signatures:

> pack_hook(tensor: Tensor) -> Any
> 
> 
> 
> 
> unpack_hook(Any) -> Tensor

where the return value of `pack_hook` is a valid input to `unpack_hook`.

In general, you want `unpack_hook(pack_hook(t))` to be equal to `t` in terms
of value, size, dtype and device.

Example:

```
>>> def pack_hook(x):
... print("Packing", x)
... return x.detach()
>>>
>>> def unpack_hook(x):
... print("Unpacking", x)
... return x
>>>
>>> a = torch.ones(5, requires_grad=True)
>>> b = torch.ones(5, requires_grad=True) * 2
>>> with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
... y = a * b
Packing tensor([1., 1., 1., 1., 1.], requires_grad=True)
Packing tensor([2., 2., 2., 2., 2.], grad_fn=<MulBackward0>)
>>> y.sum().backward()
Unpacking tensor([1., 1., 1., 1., 1.], requires_grad=True)
Unpacking tensor([2., 2., 2., 2., 2.], grad_fn=<MulBackward0>)
```

Warning

Performing an inplace operation on the input to either hooks may lead
to undefined behavior.

Warning

Only one pair of hooks is allowed at a time. When recursively nesting this
context-manager, only the inner-most pair of hooks will be applied.

Warning

To avoid reference cycle, the return value of `pack_hook` cannot hold a
reference to the input tensor. For example, use lambda x: x.detach()
instead of lambda x: x as the pack hook.

*class*torch.autograd.graph.save_on_cpu(*pin_memory=False*, *device_type='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L357)

Context manager under which tensors saved by the forward pass will be stored on cpu, then retrieved for backward.

When performing operations within this context manager, intermediary
results saved in the graph during the forward pass will be moved to CPU,
then copied back to the original device when needed for the backward pass.
If the graph was already on CPU, no tensor copy is performed.

Use this context-manager to trade compute for GPU memory usage (e.g.
when your model doesn't fit in GPU memory during training).

Warning

When `pin_memory=True`, the GPU to CPU copy during packing is
asynchronous. Accessing saved tensors on CPU (e.g. via
`grad_fn._saved_self`) before the CUDA stream has finished may
yield incorrect data. Call [`torch.cuda.synchronize()`](generated/torch.cuda.synchronize.html#torch.cuda.synchronize) first
if you need to read them.

Parameters:

**pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` tensors will be saved to CPU pinned memory
during packing and copied to GPU asynchronously during both
packing and unpacking.
Defaults to `False`.
Also see [Use pinned memory buffers](notes/cuda.html#cuda-memory-pinning).

Example:

```
>>> a = torch.randn(5, requires_grad=True, device="cuda")
>>> b = torch.randn(5, requires_grad=True, device="cuda")
>>> c = torch.randn(5, requires_grad=True, device="cuda")
>>>
>>> def f(a, b, c):
... prod_1 = a * b # a and b are saved on GPU
... with torch.autograd.graph.save_on_cpu():
... prod_2 = prod_1 * c # prod_1 and c are saved on CPU
... y = prod_2 * a # prod_2 and a are saved on GPU
... return y
>>>
>>> y = f(a, b, c)
>>> del a, b, c # for illustration only
>>> # the content of a, b, and prod_2 are still alive on GPU
>>> # the content of prod_1 and c only live on CPU
>>> y.sum().backward() # all CPU tensors are moved back to GPU, for backward
>>> # all intermediary tensors are released (deleted) after the call to backward
```

*class*torch.autograd.graph.disable_saved_tensors_hooks(*error_message*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L430)

Context-manager that disables the saved tensors default hooks feature.

Useful for if you are creating a feature that does not work with saved
tensors default hooks.

Parameters:

**error_message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - When saved tensors default hooks are used when they
have been disabled, a RuntimeError with this
error message gets raised.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

Example:

```
>>> message = "saved tensors default hooks are disabled"
>>> with torch.autograd.graph.disable_saved_tensors_hooks(message):
... # Raises RuntimeError: saved tensors default hooks are disabled
... with torch.autograd.graph.save_on_cpu():
... pass
```

*class*torch.autograd.graph.register_multi_grad_hook(*tensors*, *fn*, ***, *mode='all'*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L671)

Register a multi-grad backward hook.

There are two supported modes: `"all"` and `"any"`.

Under the `"all"` mode, the hook will be called after gradients with respect to every tensor in
`tensors` have been computed. If a tensor is in `tensors` but
is not part of the graph, or if a tensor is not needed to compute the gradients
for any `inputs` specified for the current `.backward()` or `.grad()` call,
this tensor will be ignored and the hook will not wait for its gradient to be
computed.

After every non-ignored tensor's gradient has been computed, `fn` will be
called with those gradients. `None` will be passed for tensors that did not
have their gradients computed.

Under the `"any"` mode, the hook will be called after the first gradient
with respect to a tensor in `tensors` has been computed. The hook
will be called with that gradient as its argument.

The hook should not modify its arguments.

This function returns a handle with a method `handle.remove()` that removes the hook.

Note

See [Backward Hooks execution](notes/autograd.html#backward-hooks-execution) for more information on how when this hook
is executed, and how its execution is ordered relative to other hooks.

Example:

```
>>> import torch
>>>
>>> a = torch.rand(2, 3, requires_grad=True)
>>> b = torch.rand(2, 3, requires_grad=True)
>>> c = a * b
>>> d = a * b
>>>
>>> def fn(grads):
... print([g is not None for g in grads])
...
>>> torch.autograd.graph.register_multi_grad_hook((a, b, c, d), fn)
>>>
>>> c.sum().backward(retain_graph=True)
[True, True, True, False]
>>> c.sum().backward(inputs=(a,), retain_graph=True)
[True, False, True, False]
>>>
```

Return type:

*RemovableHandle*

*class*torch.autograd.graph.node_creation_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L466)

Context-manager that registers a hook called on each autograd Node created within it.

In that context, `hook` is called once for every autograd graph node
created by operations on tensors that require grad, with the freshly
created `torch.autograd.graph.Node` as its only argument. The
intended use is to record the node, stash entries in `node.metadata`,
or register backward hooks on it via
[`register_hook()`](generated/torch.autograd.graph.Node.register_hook.html#torch.autograd.graph.Node.register_hook) and
[`register_prehook()`](generated/torch.autograd.graph.Node.register_prehook.html#torch.autograd.graph.Node.register_prehook).

The node is passed to the hook only once it is fully populated: its
`next_functions` are wired, all outputs' metadata are bound, and the
tensors saved for backward (`_saved_*`) have been stored, so a hook
that inspects the node sees its complete state.

The hook should have the following signature:

```
hook(node: torch.autograd.graph.Node) -> None
```

The registration is thread-local and propagates like other autograd
thread-local state: it is active on autograd engine worker threads, so
nodes created during backward (e.g. with `create_graph=True` or inside
checkpoint recomputation) also fire the hook.

When nesting this context-manager, every active hook is called for each
node, in registration order (outermost context-manager first). Creating
a new autograd node from inside a hook raises an error; hooks must only
observe the node they are given.

One motivating use case is attributing work done during backward to the
forward region that created the graph, by capturing state at node
creation time and restoring it around the node's backward execution:

```
>>> def creation_hook(node):
... # ``current_region()``/``enter_region()`` are user-defined and
... # stand in for whatever thread-local state you want to restore
... # while this node runs in backward.
... region = current_region()
... node.register_prehook(lambda gO: enter_region(region))
... node.register_hook(lambda gI, gO: enter_region(None))
>>>
>>> with torch.autograd.graph.node_creation_hook(creation_hook):
... loss = model(inputs)
```

Example:

```
>>> a = torch.ones(5, requires_grad=True)
>>> with torch.autograd.graph.node_creation_hook(lambda node: print(node)):
... b = a * 2
<AccumulateGrad object at ...>
<MulBackward0 object at ...>
```

Note

An `AccumulateGrad` node fires this hook when it is created, but
not when a previously created one is reused. The node is created on
demand the first time a leaf tensor is wired into a graph and is then
cached (via a weak reference) on the leaf, so it fires again only
after the old node has been freed. Since freeing the autograd graph
drops that node, code that frees the graph each iteration (the common
case) fires the hook consistently on each leaf's first use within the
context.

*class*torch.autograd.graph.allow_mutation_on_saved_tensors[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L961)

Context manager under which mutating tensors saved for backward is allowed.

Under this context manager, tensors saved for backward are cloned on mutation,
so the original version can still be used during backward. Normally, mutating a tensor
saved for backward will result in an error raised when it's used during backward.

To ensure the correct behavior, both the forward and backward should be run under
the same context manager.

Returns:

An _AllowMutationOnSavedContext object storing the state managed by this
context manager. This object can be useful for debugging purposes. The state
managed by the context manager is automatically cleared upon exiting.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[*_AllowMutationOnSavedContext*, None, None]

Example:

```
>>> import torch
>>> with torch.autograd.graph.allow_mutation_on_saved_tensors():
... # forward
... a = torch.ones(2, 3, requires_grad=True)
... b = a.clone()
... out = (b**2).sum()
... b.sin_()
... # backward
... out.sum().backward()
...
tensor([[0.8415, 0.8415, 0.8415],
 [0.8415, 0.8415, 0.8415]], grad_fn=<SinBackward0>)
```

*class*torch.autograd.graph.GradientEdge(*node*, *output_nr*, *ownership_token=None*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L210)

Object representing a given gradient edge within the autograd graph.

To get the gradient edge where a given Tensor gradient will be computed,
you can do `edge = autograd.graph.get_gradient_edge(tensor)`.

torch.autograd.graph.get_gradient_edge(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L224)

Get the gradient edge for computing the gradient of the given Tensor.

In particular, it is equivalent to call
`g = autograd.grad(loss, input)` and `g = autograd.grad(loss, get_gradient_edge(input))`.

Return type:

*GradientEdge*

torch.autograd.graph.region_activation_memory_budget(*budget*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L541)

Context-manager that sets the activation memory budget for the region of
a compiled forward traced under it.

Warning

This is a prototype feature and is subject to change.

Under [`torch.compile()`](generated/torch.compile.html#torch.compile), the min-cut partitioner chooses which
activations to save versus recompute in the backward pass to stay under a
memory budget. `budget` is a ratio in `[0, 1]`: `0.0` corresponds to
the activation memory from applying activation checkpointing to the full
region, and `1.0` corresponds to the activation memory from the default
runtime-optimized strategy. So `0.4` would result in a strategy that saves
40% of the activations compared to the default strategy. It solves a 0-1
knapsack to find the minimum recompute necessary to stay below the budget.
This overrides the global `torch._functorch.config.activation_memory_budget`
for the annotated region.

Note

Today the partitioner only supports a single budget per compiled graph,
so the annotation must cover every forward op in the graph (a partial
annotation is rejected rather than silently applied graph-wide), and all
annotated nodes must agree on the budget. To use different budgets for
different parts of a model, separate them with a graph break (e.g.
`torch._dynamo.graph_break()`) so each part becomes its own graph.

This only has an effect under [`torch.compile()`](generated/torch.compile.html#torch.compile); using it outside of a
compiled region raises a `RuntimeError`.

Parameters:

**budget** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Activation memory budget ratio in `[0, 1]`.

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)[None]

Example:

```
>>> with torch.autograd.graph.region_activation_memory_budget(0.0):
... x = layer(x) # recompute this region's activations in backward
```

torch.autograd.graph.set_warn_on_accumulate_grad_stream_mismatch(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L606)

Whether to warn when the AccumulateGrad node's stream does not match the stream
of the node that produced the incoming gradient.

torch.autograd.graph.set_override_stale_capture_stream(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/autograd/graph.py#L613)

Control behavior when autograd detects a stale non-capturing stream during
CUDA graph capture.

During CUDA graph capture, autograd nodes may reference a stale stream
that is not part of the capture. With the flag disabled (the
process-initial state), autograd raises a `RuntimeError` when the stale
stream is the default stream (stream 0), because this case always
invalidates the capture: `cudaStreamWaitEvent` on the default stream
pulls a non-capturing stream into the graph. For non-default stale streams
the stream reference is left unchanged; the capture will succeed if the
user has joined the stream into the capture (e.g. via
`capture_stream.wait_stream(stale_stream)`) and will otherwise fail with
a CUDA runtime error.

When `enabled=True`, any stale non-capturing stream (default or
non-default) is automatically overridden with the producer's capturing
stream, allowing the capture to proceed. This is a process-global setting
and is not thread-local.

The flag also governs the end-of-backward sync between each leaf's stream
and the caller's current stream. A leaf whose incoming gradients are all
undefined (e.g. patterns that compute certain gradients out of band and
return `None` from autograd) cannot be reconciled by the override, so
when exactly one of the two streams is capturing, that sync would cross
the capture boundary: with the flag enabled the sync is skipped (work on
a non-capturing stream is not part of the capture, so the ordering has no
effect on it); with the flag disabled a `RuntimeError` is raised.

Parameters:

**enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, override stale non-capturing streams with
the producer's capturing stream during CUDA graph capture, and
skip end-of-backward leaf syncs that would cross the capture
boundary. If `False` (the process-initial state), raise an error
when the stale stream is the default stream (stream 0) or when a
leaf sync would cross the capture boundary; other stale streams
are left unchanged.

| [`Variable`](generated/torch.autograd.variable.Variable.html#torch.autograd.variable.Variable) | |
| --- | --- |
| [`VariableMeta`](generated/torch.autograd.variable.VariableMeta.html#torch.autograd.variable.VariableMeta) | |