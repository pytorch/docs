# torch.utils.hipify.hipify_python.find_closure_group

torch.utils.hipify.hipify_python.find_closure_group(*input_string*, *start*, *group*)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/utils/hipify/hipify_python.py#L427)

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