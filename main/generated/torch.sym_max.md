# torch.sym_max

torch.sym_max(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/__init__.py#L890)

SymInt-aware utility for max which avoids branching on a < b.
Unlike builtins.max(), this only works for int/float, and it always
promotes to float if any argument is float (unlike builtins.max, which
will faithfully preserve the type of the input argument).