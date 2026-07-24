# torch.fx.passes.pass_manager.this_before_that_pass_constraint

torch.fx.passes.pass_manager.this_before_that_pass_constraint(*this*, *that*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/passes/pass_manager.py#L143)

Defines a partial order ('depends on' function) where this must occur
before that.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]], [bool](https://docs.python.org/3/library/functions.html#bool)]