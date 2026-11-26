# torch.utils.hipify.hipify_python.find_closure_group

torch.utils.hipify.hipify_python.find_closure_group(*input_string*, *start*, *group*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/utils/hipify/hipify_python.py#L435)

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