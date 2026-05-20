# DimDynamic

*class*torch.fx.experimental.symbolic_shapes.DimDynamic(*value*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/symbolic_shapes.py#L1967)

Controls how to perform symbol allocation for a dimension. It is always
sound to default this to DYNAMIC, but the policies DUCK and STATIC can
result in better trace-time and compile-time performance, as they reduce
the number of allocated symbols and generally make your graph more static.

NB: If we notice you've applied a constraint to the dimension, we will
force it to DYNAMIC for simplicity.

DimDynamic is controlled by a variety of higher level UX features.
Currently:

- In eager mode, the default policy is DUCK.

- The default is changed to STATIC with assume_static_by_default.
- An individual dim is marked DYNAMIC if you mark_dynamic_dim.
- In export mode, the default policy is STATIC.

- An individual dim is marked DYNAMIC if you specify it in
dynamic_shapes passed to export.