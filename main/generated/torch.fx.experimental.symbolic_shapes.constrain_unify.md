# torch.fx.experimental.symbolic_shapes.constrain_unify

torch.fx.experimental.symbolic_shapes.constrain_unify(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/symbolic_shapes.py#L1870)

Given two SymInts, constrain them so that they must be equal. NB:
this will not work with SymInts that represent nontrivial expressions
(yet!)