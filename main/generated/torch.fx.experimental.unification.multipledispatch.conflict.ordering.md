# torch.fx.experimental.unification.multipledispatch.conflict.ordering

torch.fx.experimental.unification.multipledispatch.conflict.ordering(*signatures*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/fx/experimental/unification/multipledispatch/conflict.py#L147)

A sane ordering of signatures to check, first to last
Topological sort of edges as given by `edge` and `supercedes`

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type), ...]]