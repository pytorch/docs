# EqualityConstraint

*class*torch.fx.experimental.symbolic_shapes.EqualityConstraint(*warn_only*, *source_pairs*, *derived_equalities*, *phantom_symbols*, *relaxed_sources*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/symbolic_shapes.py#L2083)

Represent and decide various kinds of equality constraints between input sources.

A "source pair" is a pair of input sources for dynamic dimensions that
are specified equal. We represent source_pairs in a union-find forest
so that we can efficiently check whether two such sources are transitively equal.

A "derived equality" relates an input source to an expression over a root.
The root can be another input source, corresponding to some dynamic dimension,
or a phantom symbol that does not directly represent any dynamic dimension. We
represent derived_equalities involving input sources in a transitively-closed map
so that we can efficiently check whether an input source is transitively equal to
a given expression over another input source.
(NOTE: In contrast, it is easy to decide whether an input source is transitively equal
to a given expression over a phantom symbol; such expressions are already in canonical
form and so the problem reduces to symbolic expression equality.)