# torch.utils.hipify.hipify_python.find_closure_group

torch.utils.hipify.hipify_python.find_closure_group(*input_string*, *start*, *group*)[[source]](https://github.com/pytorch/pytorch/blob/4581144c216b65e4e1b5c6eea26d4212239a231d/torch/utils/hipify/hipify_python.py#L426)

Generalization for finding a balancing closure group

> if group = ["(", ")"], then finds the first balanced parentheses.
> if group = ["{", "}"], then finds the first balanced bracket.

Given an input string, a starting position in the input string, and the group type,
find_closure_group returns the positions of group[0] and group[1] as a tuple.

Example

```
>>> find_closure_group("(hi)", 0, ["(", ")"])
(0, 3)
```