# torch.sym_max

torch.sym_max(*a: IntLikeType*, *b: IntLikeType*) → IntLikeType[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/__init__.py#L1235)

torch.sym_max(*a: IntLikeType | FloatLikeType*, *b: IntLikeType | FloatLikeType*) → FloatLikeType

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).