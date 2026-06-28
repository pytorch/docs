# torch.fx.passes.pass_manager.log_hook

torch.fx.passes.pass_manager.log_hook(*fn*, *level=20*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/passes/pass_manager.py#L49)

Logs callable output.

This is useful for logging output of passes. Note `inplace_wrapper` replaces
the pass output with the modified object. If we want to log the original
output, apply this wrapper before `inplace_wrapper`.

Example:

```
def my_pass(d: Dict) -> bool:
 changed = False
 if "foo" in d:
 d["foo"] = "bar"
 changed = True
 return changed

pm = PassManager(passes=[inplace_wrapper(log_hook(my_pass))])
```

Parameters:

- **fn** (*Callable**[**Type1**,**Type2**]*) -
- **level** ([*int*](https://docs.python.org/3/library/functions.html#int)) - logging level (e.g. logging.INFO)

Returns:

wrapped_fn (Callable[Type1, Type2])

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]