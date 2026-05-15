# torch.fx.passes.pass_manager.this_before_that_pass_constraint

torch.fx.passes.pass_manager.this_before_that_pass_constraint(*this*, *that*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/fx/passes/pass_manager.py#L143)

Defines a partial order ('depends on' function) where this must occur
before that.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]], [bool](https://docs.python.org/3/library/functions.html#bool)]