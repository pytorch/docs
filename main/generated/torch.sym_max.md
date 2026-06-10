# torch.sym_max

torch.sym_max(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/__init__.py#L891)

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).