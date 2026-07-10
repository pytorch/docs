# torch.fx.experimental.symbolic_shapes.constrain_unify

torch.fx.experimental.symbolic_shapes.constrain_unify(*a*, *b*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/fx/experimental/symbolic_shapes.py#L1864)

Given two SymInts, constrain them so that they must be equal. NB:
this will not work with SymInts that represent nontrivial expressions
(yet!)