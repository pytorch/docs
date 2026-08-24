# SymbolicContext

*class*torch.fx.experimental.symbolic_shapes.SymbolicContext[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/fx/experimental/symbolic_shapes.py#L2246)

Data structure specifying how we should create symbols in
`_create_symbolic_sizes_strides_storage_offset`; e.g., should
they be static or dynamic.

This is an abstract base class because we are probably going to add
another version of this that says "use exactly these SymInts, don't
allocate fresh symbols."