# torch.sym_max

torch.sym_max(*a: IntLikeType*, *b: IntLikeType*) → IntLikeType[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/__init__.py#L1325)

torch.sym_max(*a: IntLikeType | FloatLikeType*, *b: IntLikeType | FloatLikeType*) → FloatLikeType

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).