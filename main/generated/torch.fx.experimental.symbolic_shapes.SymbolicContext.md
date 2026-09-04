# SymbolicContext

*class*torch.fx.experimental.symbolic_shapes.SymbolicContext[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/symbolic_shapes.py#L2251)

Data structure specifying how we should create symbols in
`_create_symbolic_sizes_strides_storage_offset`; e.g., should
they be static or dynamic.

This is an abstract base class because we are probably going to add
another version of this that says "use exactly these SymInts, don't
allocate fresh symbols."