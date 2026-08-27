# torch.fx.experimental.symbolic_shapes.constrain_unify

torch.fx.experimental.symbolic_shapes.constrain_unify(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/symbolic_shapes.py#L1870)

Given two SymInts, constrain them so that they must be equal. NB:
this will not work with SymInts that represent nontrivial expressions
(yet!)