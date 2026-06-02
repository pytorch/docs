# torch.fx.tensor_type.is_more_precise

torch.fx.tensor_type.is_more_precise(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/fx/tensor_type.py#L101)

A binary relation denoted by <= that determines if t1 is more precise than t2.
The relation is reflexive and transitive.
returns True if t1 is more precise than t2 and False otherwise.
.. rubric:: Example

Dyn >= TensorType((1,2,3))
int >= Dyn
int >= int
TensorType((1,Dyn,3)) <= TensorType((1,2,3))

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)