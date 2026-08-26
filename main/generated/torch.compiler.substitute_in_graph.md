# torch.compiler.substitute_in_graph

torch.compiler.substitute_in_graph(*original_fn*, ***, *can_constant_fold_through=False*, *skip_signature_check=False*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/compiler/__init__.py#L248)

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
>>> import binascii
>>> binascii.b2a_base64(b"abc")
b'YWJj\n'
>>> torch.compile(
... binascii.b2a_base64, fullgraph=True
... )(b"abc") # xdoctest: +SKIP("Long tracebacks")
...
Traceback (most recent call last):
...
torch._dynamo.exc.Unsupported: ...
>>> @torch.compiler.substitute_in_graph(binascii.b2a_base64)
... def b2a_base64(data, /, *, newline=True):
... return b"YWJj\n"
...
>>> torch.compile(binascii.b2a_base64, fullgraph=True)(b"abc")
b'YWJj\n'
```