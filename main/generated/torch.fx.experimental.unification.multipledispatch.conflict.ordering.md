# torch.fx.experimental.unification.multipledispatch.conflict.ordering

torch.fx.experimental.unification.multipledispatch.conflict.ordering(*signatures*)[[source]](https://github.com/pytorch/pytorch/blob/5b1433112eb30368cb8f63b3bf0145b391ec72a5/torch/fx/experimental/unification/multipledispatch/conflict.py#L147)

A sane ordering of signatures to check, first to last
Topological sort of edges as given by `edge` and `supercedes`

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type), ...]]