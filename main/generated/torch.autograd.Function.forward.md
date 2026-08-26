# torch.autograd.Function.forward

*static*Function.forward(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/autograd/function.py#L409)

Define the forward of the custom autograd Function.

This function is to be overridden by all subclasses.
There are two ways to define forward:

Usage 1 (Combined forward and ctx):

```
@staticmethod
def forward(ctx: Any, *args: Any, **kwargs: Any) -> Any:
 pass
```

- It must accept a context ctx as the first argument, followed by any
number of arguments (tensors or other types).
- See [Combined or separate forward() and setup_context()](../notes/extending.html#combining-forward-context) for more details

Usage 2 (Separate forward and ctx):

```
@staticmethod
def forward(*args: Any, **kwargs: Any) -> Any:
 pass

@staticmethod
def setup_context(ctx: Any, inputs: Tuple[Any, ...], output: Any) -> None:
 pass
```

- The forward no longer accepts a ctx argument.
- Instead, you must also override the `torch.autograd.Function.setup_context()`
staticmethod to handle setting up the `ctx` object.
`output` is the output of the forward, `inputs` are a Tuple of inputs
to the forward.
- See [Extending torch.autograd](../notes/extending.html#extending-autograd) for more details

The context can be used to store arbitrary data that can be then
retrieved during the backward pass. Tensors should not be stored
directly on ctx (though this is not currently enforced for
backward compatibility). Instead, tensors should be saved either with
`ctx.save_for_backward()` if they are intended to be used in
`backward` (equivalently, `vjp`) or `ctx.save_for_forward()`
if they are intended to be used for in `jvp`.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)