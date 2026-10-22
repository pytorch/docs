# torch.fx.experimental.unification.multipledispatch.core.ismethod

torch.fx.experimental.unification.multipledispatch.core.ismethod(*func*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/fx/experimental/unification/multipledispatch/core.py#L86)

Is func a method?
Note that this has to work as the method is defined but before the class is
defined. At this stage methods look like functions.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)