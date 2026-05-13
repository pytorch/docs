# torch.fx.experimental.graph_gradual_typechecker.element_wise_eq

torch.fx.experimental.graph_gradual_typechecker.element_wise_eq(*n*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/fx/experimental/graph_gradual_typechecker.py#L795)

For element-wise operations and handles broadcasting.
Note that after applying broadcasting to the arguments
we are able to determine if certain dimensions have not been broadcast
if they are symbolicallu equal.

in this case, we can establish equality between those dimensions and the
corresponding output dimensions.

Note that it takes two iterations for this result. One iteration to establish
equality between certain dimensions of the operands (requiring the whole solver
including unification) and another iteration to establish equality between the operands
and the resulting type, requiring another round of constraint generation and unification.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]