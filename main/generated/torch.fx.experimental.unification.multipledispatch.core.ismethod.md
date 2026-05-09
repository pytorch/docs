# torch.fx.experimental.unification.multipledispatch.core.ismethod

torch.fx.experimental.unification.multipledispatch.core.ismethod(*func*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/fx/experimental/unification/multipledispatch/core.py#L86)

Is func a method?
Note that this has to work as the method is defined but before the class is
defined. At this stage methods look like functions.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)