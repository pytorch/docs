# torch.compiler.substitute_in_graph

torch.compiler.substitute_in_graph(*original_fn*, ***, *can_constant_fold_through=False*, *skip_signature_check=False*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/compiler/__init__.py#L156)

Register a polyfill handler for a function, usually a C function from the C extension, to be
used in place of the original function when inlining the original function in the graph.

Note

The polyfill handler is only used when inlining the original function. It is not used when
the original function is called directly. In the eager mode, the decorated function calls
the performant C function rather than the polyfill handler.

The polyfill handler is a function that will be called in place of the original function when
inlining the original function. The polyfill handler should have the same signature and the same
behavior as the original function.

Parameters:

- **original_fn** (*callable*) - The original function, usually a C function, to register a polyfill
handler for.
- **can_constant_fold_through** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether the polyfill handler can be constant
folded through. That is, if the polyfill handler is a pure function and its arguments
are constant, the result of the polyfill handler can be constant folded during the
compilation. Defaults to `False`.
- **skip_signature_check** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to skip the signature check between the
original function and the polyfill handler. Defaults to `False`.

Returns:

A decorator that registers the polyfill handler for the original function.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]]

Example:

```
>>> import operator
>>> operator.indexOf([1, 2, 3, 4, 5], 3)
2
>>> torch.compile(operator.indexOf, fullgraph=True)([1, 2, 3, 4, 5], 3)
... # xdoctest: +SKIP("Long tracebacks")
Traceback (most recent call last):
...
torch._dynamo.exc.Unsupported: ...

>>> @torch.compiler.substitute_in_graph(operator.indexOf)
... def indexOf(a, b, /):
... for i, item in enumerate(a):
... if item is b or item == b:
... return i
... raise ValueError("sequence.index(x): x not in sequence")
>>>
>>> torch.compile(operator.indexOf, fullgraph=True)([1, 2, 3, 4, 5], 3)
2
```