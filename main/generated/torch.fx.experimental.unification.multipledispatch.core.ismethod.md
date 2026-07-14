# torch.fx.experimental.unification.multipledispatch.core.ismethod

torch.fx.experimental.unification.multipledispatch.core.ismethod(*func*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/fx/experimental/unification/multipledispatch/core.py#L86)

Is func a method?
Note that this has to work as the method is defined but before the class is
defined. At this stage methods look like functions.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)