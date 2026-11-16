# SymbolicContext

*class*torch.fx.experimental.symbolic_shapes.SymbolicContext[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/experimental/symbolic_shapes.py#L2261)

Data structure specifying how we should create symbols in
`_create_symbolic_sizes_strides_storage_offset`; e.g., should
they be static or dynamic.

This is an abstract base class because we are probably going to add
another version of this that says "use exactly these SymInts, don't
allocate fresh symbols."