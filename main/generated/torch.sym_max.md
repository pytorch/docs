# torch.sym_max

torch.sym_max(*a: IntLikeType*, *b: IntLikeType*) → IntLikeType[[source]](https://github.com/pytorch/pytorch/blob/ea89e4e90dc68302e8ef5cba3ddbdaa9d50d9512/torch/__init__.py#L1245)

torch.sym_max(*a: IntLikeType | FloatLikeType*, *b: IntLikeType | FloatLikeType*) → FloatLikeType

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).