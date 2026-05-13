# torch.mutation

## user_input_mutation

Note

Tags: torch.mutation

Support Level: SUPPORTED

Original source code:

```
# mypy: allow-untyped-defs
import torch

class UserInputMutation(torch.nn.Module):
 """
 Directly mutate user input in forward
 """

 def forward(self, x):
 x.mul_(2)
 return x.cos()

example_args = (torch.randn(3, 2),)
tags = {"torch.mutation"}
model = UserInputMutation()

torch.export.export(model, example_args)
```

Result:

```
ExportedProgram:
 class GraphModule(torch.nn.Module):
 def forward(self, x: "f32[3, 2]"):
 mul_: "f32[3, 2]" = torch.ops.aten.mul_.Tensor(x, 2); x = None

 cos: "f32[3, 2]" = torch.ops.aten.cos.default(mul_); mul_ = None
 return (cos,)

Graph signature:
 # inputs
 x: USER_INPUT

 # outputs
 cos: USER_OUTPUT

Range constraints: {}
```