# torch.fx.experimental.symbolic_shapes.constrain_unify

torch.fx.experimental.symbolic_shapes.constrain_unify(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/fx/experimental/symbolic_shapes.py#L1828)

Given two SymInts, constrain them so that they must be equal. NB:
this will not work with SymInts that represent nontrivial expressions
(yet!)