# torch.library

torch.library is a collection of APIs for extending PyTorch's core library
of operators. It contains utilities for testing custom operators, creating new
custom operators, and extending operators defined with PyTorch's C++ operator
registration APIs (e.g. aten operators).

For a detailed guide on effectively using these APIs, please see
[PyTorch Custom Operators Landing Page](https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html)
for more details on how to effectively use these APIs.

## Testing custom ops

Use `torch.library.opcheck()` to test custom ops for incorrect usage of the
Python torch.library and/or C++ TORCH_LIBRARY APIs. Also, if your operator supports
training, use [`torch.autograd.gradcheck()`](autograd.html#module-torch.autograd.gradcheck) to test that the gradients are
mathematically correct.

torch.library.opcheck(*op*, *args*, *kwargs=None*, ***, *test_utils=('test_schema', 'test_autograd_registration', 'test_faketensor', 'test_aot_dispatch_dynamic')*, *raise_exception=True*, *atol=None*, *rtol=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1787)

Given an operator and some sample arguments, tests if the operator is
registered correctly.

That is, when you use the torch.library/TORCH_LIBRARY APIs to create a
custom op, you specified metadata (e.g. mutability info) about the custom op
and these APIs require that the functions you pass them satisfy certain
properties (e.g. no data pointer access in the fake/meta/abstract kernel)
`opcheck` tests these metadata and properties.

Concretely, we test the following:

- test_schema: If the schema matches the implementation of
the operator. For example: if the schema specifies a Tensor is mutated,
then we check the implementation mutates the Tensor. If the schema
specifies that we return a new Tensor, then we check that the
implementation returns a new Tensor (instead of an existing one or
a view of an existing one).
- test_autograd_registration: If the operator supports training
(autograd): we check that its autograd formula is registered via
torch.library.register_autograd or a manual registration to one
or more DispatchKey::Autograd keys. Any other DispatchKey-based
registrations may lead to undefined behavior.
- test_faketensor: If the operator has a FakeTensor kernel
(and if it is correct). The FakeTensor kernel is necessary (
but not sufficient) for the operator to work with PyTorch compilation
APIs (torch.compile/export/FX). We check that a FakeTensor kernel
(also sometimes known as a meta kernel) was registered for the
operator and that it is correct. This test takes the result of
running the operator on real tensors and the result of running
the operator on FakeTensors and checks that they have the same
Tensor metadata (sizes/strides/dtype/device/etc).
- test_aot_dispatch_dynamic: If the operator has correct behavior
with PyTorch compilation APIs (torch.compile/export/FX).
This checks that the outputs (and gradients, if applicable) are the
same under eager-mode PyTorch and torch.compile.
This test is a superset of `test_faketensor` and is an e2e test;
other things it tests are that the operator supports
functionalization and that the backward pass (if it exists) also
supports FakeTensor and functionalization.

For best results, please call `opcheck` multiple times with a
representative set of inputs. If your operator supports
autograd, please use `opcheck` with inputs with `requires_grad = True`;
if your operator supports multiple devices (e.g. CPU and CUDA), please
use `opcheck` with inputs on all supported devices.

Parameters:

- **op** (*OpOverload**|**OpOverloadPacket**|**CustomOpDef*) - The operator. Must either be a function decorated with
`torch.library.custom_op()` or an OpOverload/OpOverloadPacket
found in torch.ops.* (e.g. torch.ops.aten.sin, torch.ops.mylib.foo)
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,**...**]*) - The args to the operator
- **kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - The kwargs to the operator
- **test_utils** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - Tests that we should run. Default: all of them.
Example: ("test_schema", "test_faketensor")
- **raise_exception** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If we should raise an exception on the first
error. If False, we will return a dict with information
on if each test passed or not.
- **rtol** (*Optional**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - Relative tolerance for floating point comparisons.
If specified `atol` must also be specified.
If omitted, default values based on the `dtype` are selected
(see the table in [`torch.testing.assert_close()`](testing.html#torch.testing.assert_close)).
- **atol** (*Optional**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - Absolute tolerance for floating point comparisons.
If specified `rtol` must also be specified.
If omitted, default values based on the `dtype` are selected
(see the table in [`torch.testing.assert_close()`](testing.html#torch.testing.assert_close)).

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

Warning

opcheck and [`torch.autograd.gradcheck()`](autograd.html#module-torch.autograd.gradcheck) test different things;
opcheck tests if your usage of torch.library APIs is correct while
[`torch.autograd.gradcheck()`](autograd.html#module-torch.autograd.gradcheck) tests if your autograd formula is
mathematically correct. Use both to test custom ops that support
gradient computation.

Example

```
>>> @torch.library.custom_op("mylib::numpy_mul", mutates_args=())
>>> def numpy_mul(x: Tensor, y: float) -> Tensor:
>>> x_np = x.numpy(force=True)
>>> z_np = x_np * y
>>> return torch.from_numpy(z_np).to(x.device)
>>>
>>> @numpy_mul.register_fake
>>> def _(x, y):
>>> return torch.empty_like(x)
>>>
>>> def setup_context(ctx, inputs, output):
>>> y, = inputs
>>> ctx.y = y
>>>
>>> def backward(ctx, grad):
>>> return grad * ctx.y, None
>>>
>>> numpy_mul.register_autograd(backward, setup_context=setup_context)
>>>
>>> sample_inputs = [
>>> (torch.randn(3), 3.14),
>>> (torch.randn(2, 3, device='cuda'), 2.718),
>>> (torch.randn(1, 10, requires_grad=True), 1.234),
>>> (torch.randn(64, 64, device='cuda', requires_grad=True), 90.18),
>>> ]
>>>
>>> for args in sample_inputs:
>>> torch.library.opcheck(numpy_mul, args)
```

## Creating new custom ops in Python

Use `torch.library.custom_op()` to create new custom ops.

### Choosing the kind of custom op

When defining a custom op, first decide what aliasing and mutation behavior the
operator has. This choice determines the `mutates_args`, `tags`, return schema,
and fake-kernel behavior.

```
Does the operator mutate any Tensor input?
 |
 +-- no --> Functional operator
 | Use mutates_args=().
 | Return new Tensor objects that do not alias inputs or each other.
 |
 +-- yes --> Does it mutate the first positional Tensor argument and return it?
 |
 +-- yes --> In-place operator
 | Use tags=torch.Tag.inplace.
 | Use mutates_args with exactly the first argument name.
 | Return that same first argument.
 |
 +-- no --> Does it mutate keyword-only Tensor out= arguments and return them?
 |
 +-- yes --> out= operator
 | Use tags=torch.Tag.out.
 | Do not read from the out= tensors.
 | Put mutable output tensors after * as keyword-only args.
 | Return all out= tensors in declaration order.
 |
 +-- no --> Mutable operator
 Use mutates_args for the mutated arguments.
 Do not return mutated inputs or aliases of inputs.
```

Functional operators are the simplest and should be preferred when possible.
They should not mutate inputs, and their outputs should be fresh values that do
not alias any input or other output.

Use `tags=torch.Tag.inplace` only for the conventional in-place shape: the first
positional argument is a `Tensor`, it is the only mutated argument, and the
operator returns that same `Tensor`. For example, an inferred in-place custom op
has a schema shaped like:

```
(Tensor(a!) x, ...) -> Tensor(a!)
```

Use `tags=torch.Tag.out` only for conventional `out=` variants: all mutable
output tensors are keyword-only arguments, and the operator returns those
outputs in declaration order. The implementation must write to `out=` tensors,
but must not read from them. For example:

```
(Tensor x, *, Tensor(a!) out) -> Tensor(a!)
(Tensor x, *, Tensor(a!) out0, Tensor(b!) out1) -> (Tensor(a!), Tensor(b!))
```

In-place and `out=` custom ops get an autogenerated fake kernel from their tag
and schema. Registering a fake kernel for these ops is usually unnecessary,
though it is still allowed if you need to override the autogenerated behavior.
`out=` custom ops follow the same autograd rule as built-in `out=` operators:
they do not support automatic differentiation when any argument requires grad.

Arbitrary aliasing, such as returning an alias of an input that is not one of
the in-place or `out=` patterns above, is not supported by `custom_op`.
PyTorch compiler transforms such as functionalization need to reason precisely
about mutations and aliases, so custom op aliasing is intentionally limited to
the conventional forms described here. If your operator mutates inputs but is
not an in-place or `out=` operator, model it as a mutable operator and return no
aliases of inputs.

The same operation can have different contracts depending on how it handles its
outputs:

```
from torch import Tensor

@torch.library.custom_op(
 "mylib::add_inplace",
 mutates_args={"x"},
 tags=torch.Tag.inplace,
)
def add_inplace(x: Tensor, y: Tensor) -> Tensor:
 x.add_(y)
 return x

@torch.library.custom_op(
 "mylib::add_out",
 mutates_args={"out"},
 tags=torch.Tag.out,
)
def add_out(x: Tensor, y: Tensor, *, out: Tensor) -> Tensor:
 out.copy_(x + y)
 return out

@torch.library.custom_op("mylib::add_mutate", mutates_args={"x"})
def add_mutate(x: Tensor, y: Tensor) -> None:
 x.add_(y)
```

More details on mutation, aliasing, and transforms

`custom_op` asks for a precise mutation and aliasing contract because PyTorch
uses that contract in FakeTensor, autograd, functionalization, and
`torch.compile`.

For a functional custom op, PyTorch assumes the operator does not mutate any
input and that returned tensors are fresh values. This is the easiest kind of op
for PyTorch transforms to reason about.

For an in-place custom op, `torch.Tag.inplace` gives PyTorch a stronger and more
specific contract: the first Tensor argument is mutated and the returned Tensor
is the same object. This lets PyTorch derive the fake behavior from the schema
instead of requiring a separate fake kernel.

For an `out=` custom op, `torch.Tag.out` gives PyTorch the corresponding
`out=`-variant contract: keyword-only output tensors are mutated and returned in
schema order. The `out=` tensors are output buffers only: the implementation
must not use their current values as inputs. Like built-in `out=` operators,
these custom ops do not support automatic differentiation when any argument
requires grad.

For other mutable custom ops, use `mutates_args` to name the mutated arguments,
but do not return mutated inputs or aliases of inputs. Arbitrary aliasing is
hard for transforms because functionalization rewrites mutating programs into
functional programs and must know exactly which returned tensors share storage
with which inputs. `custom_op` therefore supports the conventional in-place and
`out=` aliasing patterns directly, but does not model arbitrary view or alias
relationships.

torch.library.custom_op(*name*, *fn=None*, */*, ***, *mutates_args*, *device_types=None*, *schema=None*, *tags=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/custom_ops.py#L66)

Wraps a function into custom operator.

Reasons why you may want to create a custom op include:
- Wrapping a third-party library or custom kernel to work with PyTorch
subsystems like Autograd.
- Preventing torch.compile/export/FX tracing from peeking inside your function.

This API is used as a decorator around a function (please see examples).
The provided function must have type hints; these are needed to interface
with PyTorch's various subsystems.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - A name for the custom op that looks like "{namespace}::{name}",
e.g. "mylib::my_linear". The name is used as the op's stable identifier
in PyTorch subsystems (e.g. torch.export, FX graphs).
To avoid name collisions, please use your project name as the namespace;
e.g. all custom ops in pytorch/fbgemm use "fbgemm" as the namespace.
- **mutates_args** (*Iterable**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*] or**"unknown"*) - The names of args that the function mutates.
This MUST be accurate, otherwise, the behavior is undefined. If "unknown",
it pessimistically assumes that all inputs to the operator are being mutated.
- **device_types** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None**|**Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - The device type(s) the function
is valid for. If no device type is provided, then the function
is used as the default implementation for all device types.
Examples: "cpu", "cuda".
When registering a device-specific implementation for an operator that accepts no Tensors,
we require the operator to have a "device: torch.device argument".
- **schema** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - A schema string for the operator. If None
(recommended) we'll infer a schema for the operator from its type
annotations. We recommend letting us infer a schema unless you
have a specific reason not to.
Example: "(Tensor x, int y) -> (Tensor, Tensor)".
- **tags** ([*Tag*](torch.html#torch.Tag)*|**Sequence**[*[*Tag*](torch.html#torch.Tag)*]**|**None*) - one or more tags to apply to the
operator. Use `torch.Tag.inplace` for operators that mutate their
first Tensor argument and return it. Use `torch.Tag.out` for
operators that mutate keyword-only output tensors and return them.
Like PyTorch's built-in `out=` operators, `torch.Tag.out`
custom ops do not support autograd.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [object](https://docs.python.org/3/library/functions.html#object)]], CustomOpDef] | *CustomOpDef*

The following types are supported for the wrapped function's input parameters:

> - Scalars: `int`, `float`, `bool`, `str`, `torch.types.Number`
> - Tensors: `torch.Tensor`
> - Enums/devices: `torch.dtype`, `torch.device`
> - Flat list of the same type: `list[torch.Tensor]`,
> `list[int]`, `list[float]`, `list[bool]`,
> `list[torch.types.Number]`
> - Optionals: `Optional` of any of the above scalar/tensor types
> - Types registered via `torch.library.register_custom_class()`

The following types are supported for the return value:

> `torch.Tensor`, `list[torch.Tensor]`, `int`, `float`,
> `bool`, `torch.types.Number`.

Note

We recommend not passing in a `schema` arg and instead letting us infer
it from the type annotations. It is error-prone to write your own schema.
You may wish to provide your own schema if our interpretation of
the type annotation is not what you want.
For more info on how to write a schema string, see
[here](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/native/README.md#func)

Examples::

```
>>> import torch
>>> from torch import Tensor
>>> from torch.library import custom_op
>>> import numpy as np
>>>
>>> @custom_op("mylib::numpy_sin", mutates_args=())
>>> def numpy_sin(x: Tensor) -> Tensor:
>>> x_np = x.cpu().numpy()
>>> y_np = np.sin(x_np)
>>> return torch.from_numpy(y_np).to(device=x.device)
>>>
>>> x = torch.randn(3)
>>> y = numpy_sin(x)
>>> assert torch.allclose(y, x.sin())
>>>
>>> # Example of a custom op that only works for one device type.
>>> @custom_op("mylib::numpy_sin_cpu", mutates_args=(), device_types="cpu")
>>> def numpy_sin_cpu(x: Tensor) -> Tensor:
>>> x_np = x.numpy()
>>> y_np = np.sin(x_np)
>>> return torch.from_numpy(y_np)
>>>
>>> x = torch.randn(3)
>>> y = numpy_sin_cpu(x)
>>> assert torch.allclose(y, x.sin())
>>>
>>> # Example of a custom op that mutates an input
>>> @custom_op("mylib::numpy_sin_inplace", mutates_args={"x"}, device_types="cpu")
>>> def numpy_sin_inplace(x: Tensor) -> None:
>>> x_np = x.numpy()
>>> np.sin(x_np, out=x_np)
>>>
>>> x = torch.randn(3)
>>> expected = x.sin()
>>> numpy_sin_inplace(x)
>>> assert torch.allclose(x, expected)
>>>
>>> # Example of a custom op with inplace semantics
>>> @custom_op(
>>> "mylib::numpy_sin_",
>>> mutates_args={"x"},
>>> device_types="cpu",
>>> tags=torch.Tag.inplace,
>>> )
>>> def numpy_sin_(x: Tensor) -> Tensor:
>>> x_np = x.numpy()
>>> np.sin(x_np, out=x_np)
>>> return x
>>>
>>> x = torch.randn(3)
>>> expected = x.sin()
>>> result = numpy_sin_(x)
>>> assert result is x
>>> assert torch.allclose(x, expected)
>>>
>>> # Example of a custom op with out= semantics
>>> @custom_op(
>>> "mylib::numpy_sin_out",
>>> mutates_args={"out"},
>>> device_types="cpu",
>>> tags=torch.Tag.out,
>>> )
>>> def numpy_sin_out(x: Tensor, *, out: Tensor) -> Tensor:
>>> x_np = x.numpy()
>>> out_np = out.numpy()
>>> np.sin(x_np, out=out_np)
>>> return out
>>>
>>> x = torch.randn(3)
>>> out = torch.empty_like(x)
>>> result = numpy_sin_out(x, out=out)
>>> assert result is out
>>> assert torch.allclose(out, x.sin())
>>>
>>> # Example of a factory function
>>> @torch.library.custom_op("mylib::bar", mutates_args={}, device_types="cpu")
>>> def bar(device: torch.device) -> Tensor:
>>> return torch.ones(3)
>>>
>>> bar("cpu")
>>>
>>> # Example of a custom op with list inputs
>>> @custom_op("mylib::weighted_sum", mutates_args=())
>>> def weighted_sum(
>>> tensors: list[Tensor],
>>> weights: list[float],
>>> ) -> Tensor:
>>> return sum(t * w for t, w in zip(tensors, weights))
>>>
>>> x = torch.randn(3)
>>> y = torch.randn(3)
>>> out = weighted_sum([x, y], [0.3, 0.7])
```

torch.library.triton_op(*name*, *fn=None*, */*, ***, *mutates_args*, *schema=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/triton.py#L296)

Create a custom operator whose implementation is backed by 1+ triton kernels.

This is a more structured way of using triton kernels with PyTorch.
Prefer using triton kernels with no `torch.library` custom operator wrappers
(like `torch.library.custom_op()`, `torch.library.triton_op()`) because
that is simpler;
only use `torch.library.custom_op()`/`torch.library.triton_op()` if you
want to create an operator that behaves like PyTorch built-in operators.
For example, you may use a `torch.library` wrapper API to define the
behavior of the triton kernel when passed a tensor subclass or under
a TorchDispatchMode.

Use `torch.library.triton_op()` instead of `torch.library.custom_op()`
when the implementation
consists of 1+ triton kernels. `torch.library.custom_op()` treats
custom operators as opaque ([`torch.compile()`](generated/torch.compile.html#torch.compile) and
[`torch.export.export()`](user_guide/torch_compiler/export/api_reference.html#torch.export.export) will never trace into them), but `triton_op`
makes the implementation visible to these subsystems, allowing them
to optimize the triton kernel(s).

Note that `fn` must only consist of calls to PyTorch-understood
operators and triton kernels. Any triton kernels called inside `fn`
must be wrapped in a call to `torch.library.wrap_triton()`.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - A name for the custom op that looks like "{namespace}::{name}",
e.g. "mylib::my_linear". The name is used as the op's stable identifier
in PyTorch subsystems (e.g. torch.export, FX graphs).
To avoid name collisions, please use your project name as the namespace;
e.g. all custom ops in pytorch/fbgemm use "fbgemm" as the namespace.
- **mutates_args** (*Iterable**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*] or**"unknown"*) - The names of args that the function mutates.
This MUST be accurate, otherwise, the behavior is undefined. If "unknown",
it pessimistically assumes that all inputs to the operator are being mutated.
- **schema** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - A schema string for the operator. If None
(recommended) we'll infer a schema for the operator from its type
annotations. We recommend letting us infer a schema unless you
have a specific reason not to.
Example: "(Tensor x, int y) -> (Tensor, Tensor)".

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)

Example:

```
>>> import torch
>>> from torch.library import triton_op, wrap_triton
>>>
>>> import triton
>>> from triton import language as tl
>>>
>>> @triton.jit
>>> def add_kernel(
>>> in_ptr0,
>>> in_ptr1,
>>> out_ptr,
>>> n_elements,
>>> BLOCK_SIZE: "tl.constexpr",
>>> ):
>>> pid = tl.program_id(axis=0)
>>> block_start = pid * BLOCK_SIZE
>>> offsets = block_start + tl.arange(0, BLOCK_SIZE)
>>> mask = offsets < n_elements
>>> x = tl.load(in_ptr0 + offsets, mask=mask)
>>> y = tl.load(in_ptr1 + offsets, mask=mask)
>>> output = x + y
>>> tl.store(out_ptr + offsets, output, mask=mask)
>>>
>>> @triton_op("mylib::add", mutates_args={})
>>> def add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
>>> output = torch.empty_like(x)
>>> n_elements = output.numel()
>>>
>>> def grid(meta):
>>> return (triton.cdiv(n_elements, meta["BLOCK_SIZE"]),)
>>>
>>> # NB: we need to wrap the triton kernel in a call to wrap_triton
>>> wrap_triton(add_kernel)[grid](x, y, output, n_elements, 16)
>>> return output
>>>
>>> @torch.compile
>>> def f(x, y):
>>> return add(x, y)
>>>
>>> x = torch.randn(3, device="cuda")
>>> y = torch.randn(3, device="cuda")
>>>
>>> z = f(x, y)
>>> assert torch.allclose(z, x + y)
```

torch.library.wrap_triton(*triton_kernel*, */*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/triton.py#L534)

Allows capture of a triton kernel into a graph via make_fx or
non-strict `torch.export`.

These technologies perform Dispatcher-based tracing (via
`__torch_dispatch__`) and cannot see calls to raw triton kernels.
The `wrap_triton` API wraps a triton kernel into a callable that
can actually be traced into a graph.

Please use this API together with `torch.library.triton_op()`.

Examples

```
>>> import torch
>>> import triton
>>> from triton import language as tl
>>> from torch.fx.experimental.proxy_tensor import make_fx
>>> from torch.library import wrap_triton
>>>
>>> @triton.jit
>>> def add_kernel(
>>> in_ptr0,
>>> in_ptr1,
>>> out_ptr,
>>> n_elements,
>>> BLOCK_SIZE: "tl.constexpr",
>>> ):
>>> pid = tl.program_id(axis=0)
>>> block_start = pid * BLOCK_SIZE
>>> offsets = block_start + tl.arange(0, BLOCK_SIZE)
>>> mask = offsets < n_elements
>>> x = tl.load(in_ptr0 + offsets, mask=mask)
>>> y = tl.load(in_ptr1 + offsets, mask=mask)
>>> output = x + y
>>> tl.store(out_ptr + offsets, output, mask=mask)
>>>
>>> def add(x, y):
>>> output = torch.empty_like(x)
>>> n_elements = output.numel()
>>>
>>> def grid_fn(meta):
>>> return (triton.cdiv(n_elements, meta["BLOCK_SIZE"]),)
>>>
>>> wrap_triton(add_kernel)[grid_fn](x, y, output, n_elements, 16)
>>> return output
>>>
>>> x = torch.randn(3, device="cuda")
>>> y = torch.randn(3, device="cuda")
>>> gm = make_fx(add)(x, y)
>>> print(gm.code)
>>> # def forward(self, x_1, y_1):
>>> # empty_like = torch.ops.aten.empty_like.default(x_1, pin_memory = False)
>>> # triton_kernel_wrapper_mutation_proxy = triton_kernel_wrapper_mutation(
>>> # kernel_idx = 0, constant_args_idx = 0,
>>> # grid = [(1, 1, 1)], kwargs = {
>>> # 'in_ptr0': x_1, 'in_ptr1': y_1, 'out_ptr': empty_like,
>>> # 'n_elements': 3, 'BLOCK_SIZE': 16
>>> # })
>>> # return empty_like
```

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

## Extending custom ops (created from Python or C++)

Use the `register.*` methods, such as `torch.library.register_kernel()` and
`torch.library.register_fake()`, to add implementations
for any operators (they may have been created using `torch.library.custom_op()` or
via PyTorch's C++ operator registration APIs).

torch.library.register_kernel(*op*, *device_types*, *func=None*, */*, ***, *lib=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1017)

Register an implementation for a device type for this operator.

Some valid device_types are: "cpu", "cuda", "xla", "mps", "ipu", "xpu".
This API may be used as a decorator.

Parameters:

- **op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**OpOverload*) - The operator to register an impl to.
- **device_types** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None**|**Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - The device_types to register an impl to.
If None, we will register to all device types - please only use
this option if your implementation is truly device-type-agnostic.
- **func** (*Callable*) - The function to register as the implementation for
the given device types.
- **lib** (*Optional**[**Library**]*) - If provided, the lifetime of this registration

Examples::

```
>>> import torch
>>> from torch import Tensor
>>> from torch.library import custom_op
>>> import numpy as np
>>>
>>> # Create a custom op that works on cpu
>>> @custom_op("mylib::numpy_sin", mutates_args=(), device_types="cpu")
>>> def numpy_sin(x: Tensor) -> Tensor:
>>> x_np = x.numpy()
>>> y_np = np.sin(x_np)
>>> return torch.from_numpy(y_np)
>>>
>>> # Add implementations for the cuda device
>>> @torch.library.register_kernel("mylib::numpy_sin", "cuda")
>>> def _(x):
>>> x_np = x.cpu().numpy()
>>> y_np = np.sin(x_np)
>>> return torch.from_numpy(y_np).to(device=x.device)
>>>
>>> x_cpu = torch.randn(3)
>>> x_cuda = x_cpu.cuda()
>>> assert torch.allclose(numpy_sin(x_cpu), x_cpu.sin())
>>> assert torch.allclose(numpy_sin(x_cuda), x_cuda.sin())
```

torch.library.register_autocast(*op*, *device_type*, *cast_inputs*, */*, ***, *lib=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1076)

Register an autocast dispatch rule for this custom op.

Valid `device_type` values include any device type that supports autocast.
See `torch.amp.is_autocast_available()` for details.

Parameters:

- **op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**OpOverload*) - The operator to register an autocast dispatch rule to.
- **device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type to use. 'cuda', 'cpu', 'xpu', or any other device type that supports autocast.
The type is the same as the type attribute of a [`torch.device`](tensor_attributes.html#torch.device).
Thus, you may obtain the device type of a tensor using Tensor.device.type.
- **cast_inputs** ([`torch.dtype`](tensor_attributes.html#torch.dtype)) - When custom op runs in an autocast-enabled region,
casts incoming floating-point Tensors to the target dtype (non-floating-point Tensors
are not affected), then executes custom op with autocast disabled.
- **lib** (*Optional**[**Library**]*) - If provided, the lifetime of this registration

Examples::

```
>>> import torch
>>> from torch import Tensor
>>> from torch.library import custom_op
>>>
>>> # Create a custom op that works on cuda
>>> @torch.library.custom_op("mylib::my_sin", mutates_args=())
>>> def my_sin(x: Tensor) -> Tensor:
>>> return torch.sin(x)
>>>
>>> # Register autocast dispatch rule for the cuda device
>>> torch.library.register_autocast("mylib::my_sin", "cuda", torch.float16)
>>>
>>> x = torch.randn(3, dtype=torch.float32, device="cuda")
>>> with torch.autocast("cuda", dtype=torch.float16):
>>> y = torch.ops.mylib.my_sin(x)
>>> assert y.dtype == torch.float16
```

torch.library.register_autograd(*op*, *backward*, */*, ***, *setup_context=None*, *lib=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1322)

Register a backward formula for this custom op.

In order for an operator to work with autograd, you need to register
a backward formula:
1. You must tell us how to compute gradients during the backward pass
by providing us a "backward" function.
2. If you need any values from the forward to compute gradients, you can
use setup_context to save values for backward.

`backward` runs during the backward pass. It accepts `(ctx, *grads)`:
- `grads` is one or more gradients. The number of gradients matches
the number of outputs of the operator.
The `ctx` object is [the same ctx object](context_method_mixins) used by
[`torch.autograd.Function`](autograd.html#torch.autograd.Function). The semantics of `backward_fn` are the
same as [`torch.autograd.Function.backward()`](generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward).

`setup_context(ctx, inputs, output)` runs during the forward pass.
Please save quantities needed for backward onto the `ctx` object via
either [`torch.autograd.function.FunctionCtx.save_for_backward()`](generated/torch.autograd.function.FunctionCtx.save_for_backward.html#torch.autograd.function.FunctionCtx.save_for_backward)
or assigning them as attributes of `ctx`. If your custom op has
kwarg-only arguments, we expect the signature of `setup_context`
to be `setup_context(ctx, inputs, keyword_only_inputs, output)`.

Both `setup_context_fn` and `backward_fn` must be traceable. That is,
they may not directly access [`torch.Tensor.data_ptr()`](generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr) and they must
not depend on or mutate global state. If you need a non-traceable backward,
you can make it a separate custom_op that you call inside `backward_fn`.

If you need different autograd behavior on different devices, then we
recommend creating two different custom operators, one for each device
that needs different behavior, and switching between them at runtime.

Examples

```
>>> import torch
>>> import numpy as np
>>> from torch import Tensor
>>>
>>> @torch.library.custom_op("mylib::numpy_sin", mutates_args=())
>>> def numpy_sin(x: Tensor) -> Tensor:
>>> x_np = x.cpu().numpy()
>>> y_np = np.sin(x_np)
>>> return torch.from_numpy(y_np).to(device=x.device)
>>>
>>> def setup_context(ctx, inputs, output) -> Tensor:
>>> x, = inputs
>>> ctx.save_for_backward(x)
>>>
>>> def backward(ctx, grad):
>>> x, = ctx.saved_tensors
>>> return grad * x.cos()
>>>
>>> torch.library.register_autograd(
... "mylib::numpy_sin", backward, setup_context=setup_context
... )
>>>
>>> x = torch.randn(3, requires_grad=True)
>>> y = numpy_sin(x)
>>> (grad_x,) = torch.autograd.grad(y, x, torch.ones_like(y))
>>> assert torch.allclose(grad_x, x.cos())
>>>
>>> # Example with a keyword-only arg
>>> @torch.library.custom_op("mylib::numpy_mul", mutates_args=())
>>> def numpy_mul(x: Tensor, *, val: float) -> Tensor:
>>> x_np = x.cpu().numpy()
>>> y_np = x_np * val
>>> return torch.from_numpy(y_np).to(device=x.device)
>>>
>>> def setup_context(ctx, inputs, keyword_only_inputs, output) -> Tensor:
>>> ctx.val = keyword_only_inputs["val"]
>>>
>>> def backward(ctx, grad):
>>> return grad * ctx.val
>>>
>>> torch.library.register_autograd(
... "mylib::numpy_mul", backward, setup_context=setup_context
... )
>>>
>>> x = torch.randn(3, requires_grad=True)
>>> y = numpy_mul(x, val=3.14)
>>> (grad_x,) = torch.autograd.grad(y, x, torch.ones_like(y))
>>> assert torch.allclose(grad_x, torch.full_like(x, 3.14))
```

torch.library.register_fake(*op*, *func=None*, */*, ***, *lib=None*, *_stacklevel=1*, *allow_override=True*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1159)

Register a FakeTensor implementation ("fake impl") for this operator.

Also sometimes known as a "meta kernel", "abstract impl".

An "FakeTensor implementation" specifies the behavior of this operator on
Tensors that carry no data ("FakeTensor"). Given some input Tensors with
certain properties (sizes/strides/storage_offset/device), it specifies
what the properties of the output Tensors are.

The FakeTensor implementation has the same signature as the operator.
It is run for both FakeTensors and meta tensors. To write a FakeTensor
implementation, assume that all Tensor inputs to the operator are
regular CPU/CUDA/Meta tensors, but they do not have storage, and
you are trying to return regular CPU/CUDA/Meta tensor(s) as output.
The FakeTensor implementation must consist of only PyTorch operations
(and may not directly access the storage or data of any input or
intermediate Tensors).

This API may be used as a decorator (see examples).

For a detailed guide on custom ops, please see
[https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html](https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html)

Parameters:

- **op_name** - Operator name (along with the overload) or OpOverload object.
- **func** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*|**None*) - Fake tensor implementation.
- **lib** (*Optional**[**Library**]*) - Library to register the fake tensor to.
- **allow_override** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Flag controlling if we want to override an
existing registered fake impl. This is on by default;
pass `False` to error if the operator already has a
fake impl. This also only applies if the custom operator
was not created via torch.library.custom_op, as
overriding an existing fake impl is already allowed.

Examples

```
>>> import torch
>>> import numpy as np
>>> from torch import Tensor
>>>
>>> # Example 1: an operator without data-dependent output shape
>>> @torch.library.custom_op("mylib::custom_linear", mutates_args=())
>>> def custom_linear(x: Tensor, weight: Tensor, bias: Tensor) -> Tensor:
>>> raise NotImplementedError("Implementation goes here")
>>>
>>> @torch.library.register_fake("mylib::custom_linear")
>>> def _(x, weight, bias):
>>> assert x.dim() == 2
>>> assert weight.dim() == 2
>>> assert bias.dim() == 1
>>> assert x.shape[1] == weight.shape[1]
>>> assert weight.shape[0] == bias.shape[0]
>>> assert x.device == weight.device
>>>
>>> return (x @ weight.t()) + bias
>>>
>>> with torch._subclasses.fake_tensor.FakeTensorMode():
>>> x = torch.randn(2, 3)
>>> w = torch.randn(3, 3)
>>> b = torch.randn(3)
>>> y = torch.ops.mylib.custom_linear(x, w, b)
>>>
>>> assert y.shape == (2, 3)
>>>
>>> # Example 2: an operator with data-dependent output shape
>>> @torch.library.custom_op("mylib::custom_nonzero", mutates_args=())
>>> def custom_nonzero(x: Tensor) -> Tensor:
>>> x_np = x.numpy(force=True)
>>> res = np.stack(np.nonzero(x_np), axis=1)
>>> return torch.tensor(res, device=x.device)
>>>
>>> @torch.library.register_fake("mylib::custom_nonzero")
>>> def _(x):
>>> # Number of nonzero-elements is data-dependent.
>>> # Since we cannot peek at the data in an fake impl,
>>> # we use the ctx object to construct a new symint that
>>> # represents the data-dependent size.
>>> ctx = torch.library.get_ctx()
>>> nnz = ctx.new_dynamic_size()
>>> shape = [nnz, x.dim()]
>>> result = x.new_empty(shape, dtype=torch.int64)
>>> return result
>>>
>>> from torch.fx.experimental.proxy_tensor import make_fx
>>>
>>> x = torch.tensor([0, 1, 2, 3, 4, 0])
>>> trace = make_fx(torch.ops.mylib.custom_nonzero, tracing_mode="symbolic")(x)
>>> trace.print_readable()
>>>
>>> assert torch.allclose(trace(x), torch.ops.mylib.custom_nonzero(x))
```

torch.library.register_vmap(*op*, *func=None*, */*, ***, *lib=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1514)

Register a vmap implementation to support [`torch.vmap()`](generated/torch.vmap.html#torch.vmap) for this custom op.

This API may be used as a decorator (see examples).

In order for an operator to work with [`torch.vmap()`](generated/torch.vmap.html#torch.vmap), you may need to register a
vmap implementation in the following signature:

> `vmap_func(info, in_dims: Tuple[Optional[int]], *args, **kwargs)`,

where `*args` and `**kwargs` are the arguments and kwargs for `op`.
We do not support kwarg-only Tensor args.

It specifies how do we compute the batched version of `op` given inputs with an additional
dimension (specified by `in_dims`).

For each arg in `args`, `in_dims` has a corresponding `Optional[int]`. It is `None`
if the arg is not a Tensor or if the arg is not being vmapped over, otherwise, it is an integer
specifying what dimension of the Tensor is being vmapped over.

`info` is a collection of additional metadata that may be helpful:
`info.batch_size` specifies the size of the dimension being vmapped over, while
`info.randomness` is the `randomness` option that was passed to [`torch.vmap()`](generated/torch.vmap.html#torch.vmap).

The return of the function `func` is a tuple of `(output, out_dims)`. Similar to `in_dims`,
`out_dims` should be of the same structure as `output` and contain one `out_dim`
per output that specifies if the output has the vmapped dimension and what index it is in.

Examples

```
>>> import torch
>>> import numpy as np
>>> from torch import Tensor
>>> from typing import Tuple
>>>
>>> def to_numpy(tensor):
>>> return tensor.cpu().numpy()
>>>
>>> lib = torch.library.Library("mylib", "FRAGMENT")
>>> @torch.library.custom_op("mylib::numpy_cube", mutates_args=())
>>> def numpy_cube(x: Tensor) -> Tuple[Tensor, Tensor]:
>>> x_np = to_numpy(x)
>>> dx = torch.tensor(3 * x_np ** 2, device=x.device)
>>> return torch.tensor(x_np ** 3, device=x.device), dx
>>>
>>> def numpy_cube_vmap(info, in_dims, x):
>>> result = numpy_cube(x)
>>> return result, (in_dims[0], in_dims[0])
>>>
>>> torch.library.register_vmap(numpy_cube, numpy_cube_vmap)
>>>
>>> x = torch.randn(3)
>>> torch.vmap(numpy_cube)(x)
>>>
>>> @torch.library.custom_op("mylib::numpy_mul", mutates_args=())
>>> def numpy_mul(x: Tensor, y: Tensor) -> Tensor:
>>> return torch.tensor(to_numpy(x) * to_numpy(y), device=x.device)
>>>
>>> @torch.library.register_vmap("mylib::numpy_mul")
>>> def numpy_mul_vmap(info, in_dims, x, y):
>>> x_bdim, y_bdim = in_dims
>>> x = x.movedim(x_bdim, -1) if x_bdim is not None else x.unsqueeze(-1)
>>> y = y.movedim(y_bdim, -1) if y_bdim is not None else y.unsqueeze(-1)
>>> result = x * y
>>> result = result.movedim(-1, 0)
>>> return result, 0
>>>
>>>
>>> x = torch.randn(3)
>>> y = torch.randn(3)
>>> torch.vmap(numpy_mul)(x, y)
```

Note

The vmap function should aim to preserve the semantics of the entire custom operator.
That is, `grad(vmap(op))` should be replaceable with a `grad(map(op))`.

If your custom operator has any custom behavior in the backward pass, please
keep this in mind.

torch.library.impl_abstract(*qualname*, *func=None*, ***, *lib=None*, *_stacklevel=1*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L973)

This API was renamed to `torch.library.register_fake()` in PyTorch 2.4.
Please use that instead.

torch.library.get_ctx()[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1696)

get_ctx() returns the current AbstractImplCtx object.

Calling `get_ctx()` is only valid inside of an fake impl
(see `torch.library.register_fake()` for more usage details.

Return type:

*FakeImplCtx*

torch.library.register_torch_dispatch(*op*, *torch_dispatch_class*, *func=None*, */*, ***, *lib=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1446)

Registers a torch_dispatch rule for the given operator and `torch_dispatch_class`.

This allows for open registration to specify the behavior between the operator
and the `torch_dispatch_class` without needing to modify the `torch_dispatch_class`
or the operator directly.

The `torch_dispatch_class` is either a Tensor subclass with `__torch_dispatch__` or a
TorchDispatchMode.

If it is a Tensor subclass, we expect `func` to have the following signature:
`(cls, func: OpOverload, types: Tuple[type, ...], args, kwargs) -> Any`

If it is a TorchDispatchMode, we expect `func` to have the following signature:
`(mode, func: OpOverload, types: Tuple[type, ...], args, kwargs) -> Any`

`args` and `kwargs` will have been normalized the same way they are
in `__torch_dispatch__` (see [__torch_dispatch__ calling convention](notes/extending.html#torch-dispatch-calling-convention)).

Examples

```
>>> import torch
>>>
>>> @torch.library.custom_op("mylib::foo", mutates_args={})
>>> def foo(x: torch.Tensor) -> torch.Tensor:
>>> return x.clone()
>>>
>>> class MyMode(torch.utils._python_dispatch.TorchDispatchMode):
>>> def __torch_dispatch__(self, func, types, args=(), kwargs=None):
>>> return func(*args, **kwargs)
>>>
>>> @torch.library.register_torch_dispatch("mylib::foo", MyMode)
>>> def _(mode, func, types, args, kwargs):
>>> x, = args
>>> return x + 1
>>>
>>> x = torch.randn(3)
>>> y = foo(x)
>>> assert torch.allclose(y, x)
>>>
>>> with MyMode():
>>> y = foo(x)
>>> assert torch.allclose(y, x + 1)
```

torch.library.infer_schema(*prototype_function*, */*, ***, *mutates_args*, *op_name=None*, *tags=()*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/infer_schema.py#L23)

Parses the schema of a given function with type hints. The schema is inferred from the
function's type hints, and can be used to define a new operator.

We make the following assumptions:

- None of the outputs alias any of the inputs or each other.
- String type annotations "device, dtype, Tensor, types" without library specification are
assumed to be torch.*. Similarly, string type annotations "Optional, List, Sequence, Union"
without library specification are assumed to be typing.*.
- Only the args listed in `mutates_args` are being mutated. If `mutates_args` is "unknown",
it assumes that all inputs to the operator are being mutates.

Callers (e.g. the custom ops API) are responsible for checking these assumptions.

Parameters:

- **prototype_function** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)) - The function from which to infer a schema for from its type annotations.
- **op_name** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - The name of the operator in the schema. If `name` is None, then the
name is not included in the inferred schema. Note that the input schema to
`torch.library.Library.define` requires an operator name.
- **mutates_args** (*"unknown"**|**Iterable**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - The arguments that are mutated in the function.
- **tags** ([*Tag*](torch.html#torch.Tag)*|**Sequence**[*[*Tag*](torch.html#torch.Tag)*]**|**None*) - one or more tags to apply to the
inferred schema. Use `torch.Tag.inplace` or `torch.Tag.out` to
infer the conventional aliasing for those operator kinds.

Returns:

The inferred schema.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

Example

```
>>> def foo_impl(x: torch.Tensor) -> torch.Tensor:
>>> return x.sin()
>>>
>>> infer_schema(foo_impl, op_name="foo", mutates_args={})
foo(Tensor x) -> Tensor
>>>
>>> infer_schema(foo_impl, mutates_args={})
(Tensor x) -> Tensor
```

*class*torch._library.custom_ops.CustomOpDef(*namespace*, *name*, *schema*, *fn*, *tags=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/custom_ops.py#L272)

CustomOpDef is a wrapper around a function that turns it into a custom op.

It has various methods for registering additional behavior for this
custom op.

You should not instantiate CustomOpDef directly; instead, use the
`torch.library.custom_op()` API.

set_kernel_enabled(*device_type*, *enabled=True*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/_library/custom_ops.py#L322)

Disable or re-enable an already registered kernel for this custom operator.

If the kernel is already disabled/enabled, this is a no-op.

Note

If a kernel is first disabled and then registered, it is disabled until enabled again.

Parameters:

- **device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The device type to disable/enable the kernel for.
- **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to disable or enable the kernel.

Example

```
>>> inp = torch.randn(1)
>>>
>>> # define custom op `f`.
>>> @custom_op("mylib::f", mutates_args=())
>>> def f(x: Tensor) -> Tensor:
>>> return torch.zeros(1)
>>>
>>> print(f(inp)) # tensor([0.]), default kernel
>>>
>>> @f.register_kernel("cpu")
>>> def _(x):
>>> return torch.ones(1)
>>>
>>> print(f(inp)) # tensor([1.]), CPU kernel
>>>
>>> # temporarily disable the CPU kernel
>>> with f.set_kernel_enabled("cpu", enabled = False):
>>> print(f(inp)) # tensor([0.]) with CPU kernel disabled
```

torch.library.get_kernel(*op*, *dispatch_key*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L1705)

Returns the computed kernel for a given operator and dispatch key.

This function retrieves the kernel that would be executed for a given
operator and dispatch key combination. The returned SafeKernelFunction
can be used to call the kernel in a boxed fashion. The intended use
case for this function is to retrieve the original kernel for a given
dispatch key and then register another kernel to the same dispatch key
that calls into the original kernel for certain cases.

Parameters:

- **op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**OpOverload**|**CustomOpDef*) - Operator name (along with the overload) or OpOverload object
Can be a string (e.g., "aten::add.Tensor"), an OpOverload, or a CustomOpDef.
- **dispatch_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**torch.DispatchKey*) - The dispatch key to get the kernel for.
Can be a string (e.g., "CPU", "CUDA") or a DispatchKey enum value.

Returns:

A safe kernel function that can be used to

call the kernel.

Return type:

torch._C._SafeKernelFunction

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If the operator does not exist.

Example

```
>>> # Get the CPU kernel for torch.add
>>> kernel = torch.library.get_kernel("aten::add.Tensor", "CPU")
>>>
>>> # You can also use DispatchKey enum
>>> kernel = torch.library.get_kernel("aten::add.Tensor", torch.DispatchKey.CPU)
>>>
>>> # Or use an OpOverload directly
>>> kernel = torch.library.get_kernel(torch.ops.aten.add.Tensor, "CPU")
>>>
>>> # Example: Using get_kernel in a custom op with conditional dispatch
>>> # Get the original kernel for torch.sin
>>> original_sin_kernel = torch.library.get_kernel("aten::sin", "CPU")
>>>
>>> # If input has negative values, use original sin, otherwise return zeros
>>> def conditional_sin_impl(dispatch_keys, x):
>>> if (x < 0).any():
>>> return original_sin_kernel.call_boxed(dispatch_keys, x)
>>> else:
>>> return torch.zeros_like(x)
>>>
>>> lib = torch.library.Library("aten", "IMPL")
>>> # with_keyset=True so the first argument to the impl is the current DispatchKeySet
>>> which needs to be the first argument to ``kernel.call_boxed``
>>> lib.impl("sin", conditional_sin_impl, "CPU", with_keyset=True)
>>>
>>> # Test the conditional behavior
>>> x_positive = torch.tensor([1.0, 2.0])
>>> x_mixed = torch.tensor([-1.0, 2.0])
>>> torch.sin(x_positive)
tensor([0., 0.])
>>> torch.sin(x_mixed)
tensor([-0.8415, 0.9093])
```

## Low-level APIs

The following APIs are direct bindings to PyTorch's C++ low-level
operator registration APIs.

Warning

The low-level operator registration APIs and the PyTorch Dispatcher are a complicated PyTorch concept. We recommend you use the higher level APIs above (that do not require a torch.library.Library object) when possible. [This blog post](http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/) is a good starting point to learn about the PyTorch Dispatcher.

A tutorial that walks you through some examples on how to use this API is available on [Google Colab](https://colab.research.google.com/drive/1RRhSfk7So3Cn02itzLWE9K4Fam-8U011?usp=sharing).

*class*torch.library.Library(*ns*, *kind*, *dispatch_key=''*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L212)

A class to create libraries that can be used to register new operators or
override operators in existing libraries from Python.
A user can optionally pass in a dispatch keyname if they only want to register
kernels corresponding to only one specific dispatch key.

To create a library to override operators in an existing library (with name ns), set the kind to "IMPL".
To create a new library (with name ns) to register new operators, set the kind to "DEF".
To create a fragment of a possibly existing library to register operators (and bypass
the limitation that there is only one library for a given namespace), set the kind to
"FRAGMENT".

Parameters:

- **ns** - library name
- **kind** - "DEF", "IMPL", "FRAGMENT"
- **dispatch_key** - PyTorch dispatch key (default: "")

define(*schema*, *alias_analysis=''*, ***, *tags=()*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L272)

Defines a new operator and its semantics in the ns namespace.

Parameters:

- **schema** - function schema to define a new operator.
- **alias_analysis** (*optional*) - Indicates if the aliasing properties of the operator arguments can be
inferred from the schema (default behavior) or not ("CONSERVATIVE").
- **tags** ([*Tag*](torch.html#torch.Tag)*|**Sequence**[*[*Tag*](torch.html#torch.Tag)*]*) - one or more torch.Tag to apply to this
operator. Tagging an operator changes the operator's behavior
under various PyTorch subsystems; please read the docs for the
torch.Tag carefully before applying it.

Returns:

name of the operator as inferred from the schema.

Example:

```
>>> my_lib = Library("mylib", "DEF")
>>> my_lib.define("sum(Tensor self) -> Tensor")
```

fallback(*fn*, *dispatch_key=''*, ***, *with_keyset=False*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L551)

Registers the function implementation as the fallback for the given key.

This function only works for a library with global namespace ("_").

Parameters:

- **fn** - function used as fallback for the given dispatch key or `fallthrough_kernel()`
to register a fallthrough.
- **dispatch_key** - dispatch key that the input function should be registered for. By default, it uses
the dispatch key that the library was created with.
- **with_keyset** - flag controlling if the current dispatcher call keyset should be passed as the first argument
to `fn` when calling. This should be used to create the appropriate keyset for redispatch calls.

Example:

```
>>> my_lib = Library("_", "IMPL")
>>> def fallback_kernel(op, *args, **kwargs):
>>> # Handle all autocast ops generically
>>> # ...
>>> my_lib.fallback(fallback_kernel, "Autocast")
```

impl(*op_name*, *fn*, *dispatch_key=''*, ***, *with_keyset=False*, *allow_override=True*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L441)

Registers the function implementation for an operator defined in the library.

Parameters:

- **op_name** - operator name (along with the overload) or OpOverload object.
- **fn** - function that's the operator implementation for the input dispatch key or `fallthrough_kernel()`
to register a fallthrough.
- **dispatch_key** - dispatch key that the input function should be registered for. By default, it uses
the dispatch key that the library was created with.
- **with_keyset** - flag controlling if the current dispatcher call keyset should be passed as the first argument
to `fn` when calling. This should be used to create the appropriate keyset for redispatch calls.
- **allow_override** - Flag controlling if we want to override an
existing registered kernel implementation. This is on
by default; pass `False` to error if a kernel is
already registered for this dispatch key.

Example::

```
>>> my_lib = Library("aten", "IMPL")
>>> def div_cpu(self, other):
>>> return self * (1 / other)
>>> my_lib.impl("div.Tensor", div_cpu, "CPU")
```

register_symm_mem_args(*op_name*, *arg_names*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L518)

Registers which arguments require symmetric memory allocation for an operator.

This method allows operators to declaratively specify which arguments need
symmetric memory treatment. When used with `torch.compile`, Inductor
automatically allocates these arguments in P2P-accessible NVLink memory
(`empty_strided_p2p`), enabling zero-copy inter-GPU communication.

The operator's schema should include a `group_name` (`str`) argument.
Inductor's `FallbackKernel._maybe_realize_symm_mem_args` extracts
`group_name` at compile time to allocate P2P buffers for the correct
process group. Without `group_name`, the automatic realization is skipped.

Parameters:

- **op_name** - operator name (along with the overload) or OpOverload object.
- **arg_names** - list of argument names that require symmetric memory allocation.

Example::

```
>>> my_lib = Library("symm_mem", "FRAGMENT")
>>> my_lib.define("one_shot_all_reduce(Tensor input, str reduce_op, str group_name) -> Tensor")
>>> my_lib.register_symm_mem_args("one_shot_all_reduce", ["input"])
```

torch.library.fallthrough_kernel()[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L60)

A dummy function to pass to `Library.impl` in order to register a fallthrough.

torch.library.define(*qualname*, *schema*, ***, *lib=None*, *tags=()*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L694)

torch.library.define(*lib*, *schema*, *alias_analysis=''*)

Defines a new operator.

In PyTorch, defining an op (short for "operator") is a two step-process:
- we need to define the op (by providing an operator name and schema)
- we need to implement behavior for how the operator interacts with
various PyTorch subsystems, like CPU/CUDA Tensors, Autograd, etc.

This entrypoint defines the custom operator (the first step)
you must then perform the second step by calling various
`impl_*` APIs, like `torch.library.impl()` or
`torch.library.register_fake()`.

Parameters:

- **qualname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The qualified name for the operator. Should be
a string that looks like "namespace::name", e.g. "aten::sin".
Operators in PyTorch need a namespace to
avoid name collisions; a given operator may only be created once.
If you are writing a Python library, we recommend the namespace to
be the name of your top-level module.
- **schema** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The schema of the operator. E.g. "(Tensor x) -> Tensor"
for an op that accepts one Tensor and returns one Tensor. It does
not contain the operator name (that is passed in `qualname`).
- **lib** (*Optional**[**Library**]*) - If provided, the lifetime of this operator
will be tied to the lifetime of the Library object.
- **tags** ([*Tag*](torch.html#torch.Tag)*|**Sequence**[*[*Tag*](torch.html#torch.Tag)*]*) - one or more torch.Tag to apply to this
operator. Tagging an operator changes the operator's behavior
under various PyTorch subsystems; please read the docs for the
torch.Tag carefully before applying it.

Example::

```
>>> import torch
>>> import numpy as np
>>>
>>> # Define the operator
>>> torch.library.define("mylib::sin", "(Tensor x) -> Tensor")
>>>
>>> # Add implementations for the operator
>>> @torch.library.impl("mylib::sin", "cpu")
>>> def f(x):
>>> return torch.from_numpy(np.sin(x.numpy()))
>>>
>>> # Call the new operator from torch.ops.
>>> x = torch.randn(3)
>>> y = torch.ops.mylib.sin(x)
>>> assert torch.allclose(y, x.sin())
```

torch.library.impl(*lib*, *name*, *dispatch_key=''*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/library.py#L804)

torch.library.impl(*qualname: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *types: [str](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[[str](https://docs.python.org/3/library/stdtypes.html#str)]*, *func: [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *lib: Library | [None](https://docs.python.org/3/library/constants.html#None) = None*) → Callable[[Callable[..., [object](https://docs.python.org/3/library/functions.html#object)]], [None](https://docs.python.org/3/library/constants.html#None)]

torch.library.impl(*qualname: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *types: [str](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[[str](https://docs.python.org/3/library/stdtypes.html#str)]*, *func: Callable[..., [object](https://docs.python.org/3/library/functions.html#object)]*, ***, *lib: Library | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [None](https://docs.python.org/3/library/constants.html#None)

torch.library.impl(*lib: Library*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *dispatch_key: [str](https://docs.python.org/3/library/stdtypes.html#str) = ''*) → Callable[[Callable[_P, _T]], Callable[_P, _T]]

Register an implementation for a device type for this operator.

You may pass "default" for `types` to register this implementation as the
default implementation for ALL device types.
Please only use this if the implementation truly supports all device types;
for example, this is true if it is a composition of built-in PyTorch operators.

This API may be used as a decorator. You can use nested decorators
with this API provided they return a function and are placed inside
this API (see Example 2).

Some valid types are: "cpu", "cuda", "xla", "mps", "ipu", "xpu".

Parameters:

- **qualname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Should be a string that looks like "namespace::operator_name".
- **types** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - The device types to register an impl to.
- **lib** (*Optional**[**Library**]*) - If provided, the lifetime of this registration
will be tied to the lifetime of the Library object.

Examples

```
>>> import torch
>>> import numpy as np
>>> # Example 1: Register function.
>>> # Define the operator
>>> torch.library.define("mylib::mysin", "(Tensor x) -> Tensor")
>>>
>>> # Add implementations for the cpu device
>>> @torch.library.impl("mylib::mysin", "cpu")
>>> def f(x):
>>> return torch.from_numpy(np.sin(x.numpy()))
>>>
>>> x = torch.randn(3)
>>> y = torch.ops.mylib.mysin(x)
>>> assert torch.allclose(y, x.sin())
>>>
>>> # Example 2: Register function with decorator.
>>> def custom_decorator(func):
>>> def wrapper(*args, **kwargs):
>>> return func(*args, **kwargs) + 1
>>> return wrapper
>>>
>>> # Define the operator
>>> torch.library.define("mylib::sin_plus_one", "(Tensor x) -> Tensor")
>>>
>>> # Add implementations for the operator
>>> @torch.library.impl("mylib::sin_plus_one", "cpu")
>>> @custom_decorator
>>> def f(x):
>>> return torch.from_numpy(np.sin(x.numpy()))
>>>
>>> # Call the new operator from torch.ops.
>>> x = torch.randn(3)
>>>
>>> y1 = torch.ops.mylib.sin_plus_one(x)
>>> y2 = torch.sin(x) + 1
>>> assert torch.allclose(y1, y2)
```