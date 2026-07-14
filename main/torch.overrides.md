# torch.overrides

This module exposes various helper functions for the `__torch_function__`
protocol. See [Extending torch Python API](notes/extending.html#extending-torch-python) for more details on the
`__torch_function__` protocol.

## Functions

torch.overrides.get_ignored_functions()[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L103)

Return public functions that cannot be overridden by `__torch_function__`.

Returns:

A tuple of functions that are publicly available in the torch API but cannot
be overridden with `__torch_function__`. Mostly this is because none of the
arguments of these functions are tensors or tensor-likes.

Return type:

[set](https://docs.python.org/3/library/stdtypes.html#set)[Callable]

Examples

```
>>> torch.Tensor.as_subclass in torch.overrides.get_ignored_functions()
True
>>> torch.add in torch.overrides.get_ignored_functions()
False
```

torch.overrides.get_overridable_functions()[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1945)

List functions that are overridable via __torch_function__

Returns:

A dictionary that maps namespaces that contain overridable functions
to functions in that namespace that can be overridden.

Return type:

Dict[Any, List[Callable]]

torch.overrides.resolve_name(*f*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1958)

Get a human readable string name for a function passed to
__torch_function__

Parameters:

**f** (*Callable*) - Function to resolve the name of.

Returns:

Name of the function; if eval'ed it should give back the input
function.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

torch.overrides.get_testing_overrides()[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L423)

Return a dict containing dummy overrides for all overridable functions

Returns:

A dictionary that maps overridable functions in the PyTorch API to
lambda functions that have the same signature as the real function
and unconditionally return -1. These lambda functions are useful
for testing API coverage for a type that defines `__torch_function__`.

Return type:

Dict[Callable, Callable]

Examples

```
>>> import inspect
>>> my_add = torch.overrides.get_testing_overrides()[torch.add]
>>> inspect.signature(my_add)
<Signature (input, other, out=None)>
```

torch.overrides.handle_torch_function(*public_api*, *relevant_args*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1722)

Implement a function with checks for `__torch_function__` overrides.

See torch::autograd::handle_torch_function for the equivalent of this
function in the C++ implementation.

Parameters:

- **public_api** (*function*) - Function exposed by the public torch API originally called like
`public_api(*args, **kwargs)` on which arguments are now being
checked.
- **relevant_args** (*iterable*) - Iterable of arguments to check for __torch_function__ methods.
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Arbitrary positional arguments originally passed into `public_api`.
- **kwargs** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Arbitrary keyword arguments originally passed into `public_api`.

Returns:

Result from calling `implementation` or an `__torch_function__`
method, as appropriate.

Return type:

[object](https://docs.python.org/3/library/functions.html#object)

:raises TypeError : if no implementation is found.:

Example

```
>>> def func(a):
... if has_torch_function_unary(a):
... return handle_torch_function(func, (a,), a)
... return a + 0
```

torch.overrides.has_torch_function()[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1811)

Check for __torch_function__ implementations in the elements of an iterable
or if a __torch_function__ mode is enabled. Considers exact `Tensor` s
and `Parameter` s non-dispatchable. Use this to guard a call to
`handle_torch_function()`; don't use it to test if something
is Tensor-like, use `is_tensor_like()` instead.
:param relevant_args: Iterable of arguments to check for __torch_function__ methods.
:type relevant_args: iterable

Returns:

True if any of the elements of relevant_args have __torch_function__
implementations, False otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

See also

`torch.is_tensor_like`

Checks if something is a Tensor-like, including an exact `Tensor`.

torch.overrides.is_tensor_like(*inp*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L2013)

Returns `True` if the passed-in input is a Tensor-like.

Currently, this occurs whenever there's a `__torch_function__`
attribute on the type of the input.

Examples

A subclass of tensor is generally a Tensor-like.

```
>>> class SubTensor(torch.Tensor): ...
>>> is_tensor_like(SubTensor([0]))
True
```

Built-in or user types aren't usually Tensor-like.

```
>>> is_tensor_like(6)
False
>>> is_tensor_like(None)
False
>>> class NotATensor: ...
>>> is_tensor_like(NotATensor())
False
```

But, they can be made Tensor-like by implementing __torch_function__.

```
>>> class TensorLike:
... @classmethod
... def __torch_function__(cls, func, types, args, kwargs):
... return -1
>>> is_tensor_like(TensorLike())
True
```

torch.overrides.is_tensor_method_or_property(*func*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1987)

Returns True if the function passed in is a handler for a
method or property belonging to `torch.Tensor`, as passed
into `__torch_function__`.

Note

For properties, their `__get__` method must be passed in.

This may be needed, in particular, for the following reasons:

1. Methods/properties sometimes don't contain a __module__ slot.
2. They require that the first passed-in argument is an instance
of `torch.Tensor`.

Examples

```
>>> is_tensor_method_or_property(torch.Tensor.add)
True
>>> is_tensor_method_or_property(torch.add)
False
```

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.overrides.wrap_torch_function(*dispatcher*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L1601)

Wraps a given function with `__torch_function__` -related functionality.

Parameters:

**dispatcher** (*Callable*) - A callable that returns an iterable of Tensor-likes passed into the function.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]]

Note

This decorator may reduce the performance of your code. Generally, it's enough to express
your code as a series of functions that, themselves, support __torch_function__. If you
find yourself in the rare situation where this is not the case, e.g. if you're wrapping a
low-level library and you also need it to work for Tensor-likes, then this function is available.

Examples

```
>>> def dispatcher(a): # Must have the same signature as func
... return (a,)
>>> @torch.overrides.wrap_torch_function(dispatcher)
>>> def func(a): # This will make func dispatchable by __torch_function__
... return a + 0
```

torch.overrides.redispatch_function(*func*, *types*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/overrides.py#L2168)

Skip one level of `__torch_function__` dispatch and call the function.

This is primarily useful for **Tensor subclasses** that want to call into
a function's implementation while still intercepting PyTorch operations
inside that function.

Example with Tensor subclass. Only ops whose inputs include a
`LoggingTensor` are intercepted; once `redispatch_function` returns
a plain `torch.Tensor`, subsequent ops (here `+ 1`) are not logged.

```
>>> from torch.overrides import has_torch_function, handle_torch_function
>>> class LoggingTensor(torch.Tensor):
... depth = 0
...
... @classmethod
... def __torch_function__(cls, func, types, args, kwargs=None):
... print(f"{' ' * cls.depth}Calling {func.__name__}")
... cls.depth += 1
... r = torch.overrides.redispatch_function(func, types, args, kwargs)
... cls.depth -= 1
... return r
>>> def scaled_mul(a, b):
... if has_torch_function((a, b)):
... return handle_torch_function(scaled_mul, (a, b), a, b)
... return a * b + 1
>>> x = LoggingTensor(torch.tensor([3.0]))
>>> y = LoggingTensor(torch.tensor([4.0]))
>>> result = scaled_mul(x, y)
Calling scaled_mul
 Calling mul
>>> result
tensor([13.])
```

Note that only `mul` is logged, not `add`: `redispatch_function`
returns a plain `torch.Tensor`, so the `+ 1` inside `scaled_mul`
no longer sees a `LoggingTensor` input and `__torch_function__` is
not triggered.

With `TorchFunctionMode` the mode stays active across all inner ops,
so the `+ 1` is now visible too. Use `with self:` after
`redispatch_function` to re-enable the mode for those inner calls.

```
>>> from torch.overrides import TorchFunctionMode
>>> class LoggingMode(TorchFunctionMode):
... def __init__(self):
... self.depth = 0
...
... def __torch_function__(self, func, types, args, kwargs=None):
... print(f"{' ' * self.depth}Calling {func.__name__}")
... self.depth += 1
... with self:
... r = torch.overrides.redispatch_function(
... func, types, args, kwargs
... )
... self.depth -= 1
... return r
>>> a = torch.tensor([3.0])
>>> b = torch.tensor([4.0])
>>> with LoggingMode():
... result = scaled_mul(a, b)
Calling scaled_mul
 Calling mul
 Calling add
>>> result
tensor([13.])
```