# torch.sym_max

torch.sym_max(*a: IntLikeType*, *b: IntLikeType*) → IntLikeType[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/__init__.py#L1245)

torch.sym_max(*a: IntLikeType | FloatLikeType*, *b: IntLikeType | FloatLikeType*) → FloatLikeType

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).