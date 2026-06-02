# torch.fx.experimental.unification.multipledispatch.conflict.ordering

torch.fx.experimental.unification.multipledispatch.conflict.ordering(*signatures*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/fx/experimental/unification/multipledispatch/conflict.py#L147)

A sane ordering of signatures to check, first to last
Topological sort of edges as given by `edge` and `supercedes`

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]