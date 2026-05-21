# torch.fx.passes.pass_manager.these_before_those_pass_constraint

torch.fx.passes.pass_manager.these_before_those_pass_constraint(*these*, *those*)[[source]](https://github.com/pytorch/pytorch/blob/1af0b90bbfa06b98936ac35f25070579cffc8d74/torch/fx/passes/pass_manager.py#L157)

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

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]], [bool](https://docs.python.org/3/library/functions.html#bool)]