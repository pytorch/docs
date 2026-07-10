# SymbolicContext

*class*torch.fx.experimental.symbolic_shapes.SymbolicContext[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/fx/experimental/symbolic_shapes.py#L2245)

Data structure specifying how we should create symbols in
`_create_symbolic_sizes_strides_storage_offset`; e.g., should
they be static or dynamic.

This is an abstract base class because we are probably going to add
another version of this that says "use exactly these SymInts, don't
allocate fresh symbols."