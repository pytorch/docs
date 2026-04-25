# torch.fx.experimental.symbolic_shapes.constrain_unify

torch.fx.experimental.symbolic_shapes.constrain_unify(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/fx/experimental/symbolic_shapes.py#L1828)

Given two SymInts, constrain them so that they must be equal. NB:
this will not work with SymInts that represent nontrivial expressions
(yet!)