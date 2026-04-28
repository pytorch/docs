# torch.fx.experimental.unification.multipledispatch.core.ismethod

torch.fx.experimental.unification.multipledispatch.core.ismethod(*func*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/fx/experimental/unification/multipledispatch/core.py#L86)

Is func a method?
Note that this has to work as the method is defined but before the class is
defined. At this stage methods look like functions.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)