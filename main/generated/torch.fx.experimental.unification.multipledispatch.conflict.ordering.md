# torch.fx.experimental.unification.multipledispatch.conflict.ordering

torch.fx.experimental.unification.multipledispatch.conflict.ordering(*signatures*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/experimental/unification/multipledispatch/conflict.py#L147)

A sane ordering of signatures to check, first to last
Topological sort of edges as given by `edge` and `supercedes`

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]