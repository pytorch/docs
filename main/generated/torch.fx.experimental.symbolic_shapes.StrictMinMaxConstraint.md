# StrictMinMaxConstraint

*class*torch.fx.experimental.symbolic_shapes.StrictMinMaxConstraint(*warn_only*, *vr*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/fx/experimental/symbolic_shapes.py#L2023)

For clients: the size at this dimension must be within 'vr' (which
specifies a lower and upper bound, inclusive-inclusive) AND it
must be non-negative and should not be 0 or 1 (but see NB below).

For backends: there must not be any guards on this dimension which
are not implied by the given lower and upper bound. Regardless of
the lower bound, the backend can assume the size is non-negative
and that it is not 0 or 1.

An unbounded StrictMinMaxConstraint can be thought of as a strict version
of "RelaxedUnspecConstraint".

NB: Export will often unsoundly assume that a graph works for 0/1, even
though at trace time we assumed size is not 0 or 1. The idea is that
if we produce a graph that works for a range of values, it will be OK
for N=0/1 too.

render(*source*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/fx/experimental/symbolic_shapes.py#L2046)

Format the constrain equation

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)