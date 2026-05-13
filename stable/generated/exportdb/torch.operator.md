# torch.operator

## unsupported_operator

Note

Tags: torch.operator

Support Level: SUPPORTED

Original source code:

```
# mypy: allow-untyped-defs
import torch
from torch._export.db.case import SupportLevel

class TorchSymMin(torch.nn.Module):
 """
 torch.sym_min operator is supported in export.
 """

 def forward(self, x):
 return x.sum() + torch.sym_min(x.size(0), 100)

example_args = (torch.randn(3, 2),)
tags = {"torch.operator"}
support_level = SupportLevel.SUPPORTED
model = TorchSymMin()

torch.export.export(model, example_args)
```

Result:

```
ExportedProgram:
 class GraphModule(torch.nn.Module):
 def forward(self, x: "f32[3, 2]"):
 sum_1: "f32[]" = torch.ops.aten.sum.default(x); x = None
 add: "f32[]" = torch.ops.aten.add.Tensor(sum_1, 3); sum_1 = None
 return (add,)

Graph signature:
 # inputs
 x: USER_INPUT

 # outputs
 add: USER_OUTPUT

Range constraints: {}
```