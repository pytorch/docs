# torch.fx.passes.pass_manager.this_before_that_pass_constraint

torch.fx.passes.pass_manager.this_before_that_pass_constraint(*this*, *that*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/fx/passes/pass_manager.py#L143)

Defines a partial order ('depends on' function) where this must occur
before that.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]], [bool](https://docs.python.org/3/library/functions.html#bool)]