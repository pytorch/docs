# torch.fx.tensor_type.is_consistent

torch.fx.tensor_type.is_consistent(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/fx/tensor_type.py#L72)

A binary relation denoted by ~ that determines if t1 is consistent with t2.
The relation is reflexive, symmetric but not transitive.
returns True if t1 and t2 are consistent and False otherwise.
.. rubric:: Example

Dyn ~ TensorType((1,2,3))
int ~ Dyn
int ~ int
TensorType((1,Dyn,3)) ~ TensorType((1,2,3))

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)