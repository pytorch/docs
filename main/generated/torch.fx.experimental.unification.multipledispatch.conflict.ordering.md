# torch.fx.experimental.unification.multipledispatch.conflict.ordering

torch.fx.experimental.unification.multipledispatch.conflict.ordering(*signatures*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/fx/experimental/unification/multipledispatch/conflict.py#L147)

A sane ordering of signatures to check, first to last
Topological sort of edges as given by `edge` and `supercedes`

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]