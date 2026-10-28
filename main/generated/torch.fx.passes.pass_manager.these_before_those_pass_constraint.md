# torch.fx.passes.pass_manager.these_before_those_pass_constraint

torch.fx.passes.pass_manager.these_before_those_pass_constraint(*these*, *those*)[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/fx/passes/pass_manager.py#L157)

Defines a partial order ('depends on' function) where `these` must occur
before `those`. Where the inputs are 'unwrapped' before comparison.

For example, the following pass list and constraint list would be invalid:

```
passes = [
 loop_pass(pass_b, 3),
 loop_pass(pass_a, 5),
]

constraints = [these_before_those_pass_constraint(pass_a, pass_b)]
```

Parameters:

- **these** (*Callable*) - pass which should occur first
- **those** (*Callable*) - pass which should occur later

Returns:

depends_on (Callable[[Object, Object], bool])

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]], [bool](https://docs.python.org/3/builtins/functions.html#bool)]