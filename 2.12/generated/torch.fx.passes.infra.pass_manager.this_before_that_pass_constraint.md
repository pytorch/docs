# torch.fx.passes.infra.pass_manager.this_before_that_pass_constraint

torch.fx.passes.infra.pass_manager.this_before_that_pass_constraint(*this*, *that*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/passes/infra/pass_manager.py#L124)

Defines a partial order ('depends on' function) where `this` must occur
before `that`.

For example, the following pass list and constraint list would be invalid:

```
passes = [pass_b, pass_a]

constraints = [this_before_that_pass_constraint(pass_a, pass_b)]
```

Parameters:

- **this** (*Callable*) - pass which should occur first
- **that** (*Callable*) - pass which should occur later

Returns:

depends_on (Callable[[Object, Object], bool])

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)

Warning

This API is experimental and is *NOT* backward-compatible.