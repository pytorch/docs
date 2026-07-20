# Control Flow - Switch

`torch.switch` is a structured control flow operator for multi-way branching. It can be used to specify
switch-case like control flow and can logically be seen as implemented as follows:

```
def switch(
 index: Union[int, torch.Tensor],
 branches: Tuple[Callable, ...],
 operands: Tuple[torch.Tensor]
):
 return branches[index](*operands)
```

Its unique power lies in its ability to express **data-dependent multi-way control flow**: it lowers to a
switch operator (`torch.ops.higher_order.switch`), which preserves the index, all branch functions, and operands.
This enables efficient compilation and deployment of models with N-way branching based on the **value** or
**shape** of inputs or intermediate outputs.

Warning

`torch.switch` is a prototype feature in PyTorch. It has limited support for input and output types.
Please look forward to a more stable implementation in a future version of PyTorch.
Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

## Examples

Below is an example that uses switch to select between multiple operations based on an input index:

```
import torch
from torch._higher_order_ops.switch import switch

def branch0(x: torch.Tensor):
 return x.cos()

def branch1(x: torch.Tensor):
 return x.sin()

def branch2(x: torch.Tensor):
 return x.tan()

class BasicSwitch(torch.nn.Module):
 """
 A basic usage of switch with multiple branches.
 """

 def __init__(self):
 super().__init__()

 def forward(self, index: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
 return switch(index, [branch0, branch1, branch2], (x,))

switch_mod = BasicSwitch()
```

We can eagerly run the model and expect the results vary based on the index:

```
x = torch.randn(3)
idx0 = torch.tensor(0)
idx1 = torch.tensor(1)
idx2 = torch.tensor(2)
print(switch_mod(idx0, x), branch0(x))
print(switch_mod(idx1, x), branch1(x))
print(switch_mod(idx2, x), branch2(x))
```

We can export the model for further transformations and deployment:

```
x = torch.randn(4, 3)
idx = torch.tensor(1)
ep = torch.export.export(
 BasicSwitch(),
 (idx, x),
 dynamic_shapes={"index": None, "x": {0: torch.export.Dim.DYNAMIC}}
)
print(ep)
```

Notice that `torch.switch` is lowered to `torch.ops.higher_order.switch`, and branch functions become
sub-graph attributes of the top level graph module.

Here is another example showcasing switch with data-dependent index:

```
def branch0(x: torch.Tensor):
 return x * 2

def branch1(x: torch.Tensor):
 return x + 10

def branch2(x: torch.Tensor):
 return x ** 2

class DataDependentSwitch(torch.nn.Module):
 """
 A usage of switch with data-dependent index.
 """
 def __init__(self):
 super().__init__()

 def forward(self, x: torch.Tensor) -> torch.Tensor:
 # Select branch based on the sign of the sum
 index = torch.clamp((x.sum() > 0).long() + (x.sum() > 5).long(), 0, 2)
 return switch(index, [branch0, branch1, branch2], (x,))

x = torch.randn(4, 3)
ep = torch.export.export(
 DataDependentSwitch(),
 (x,),
 dynamic_shapes={"x": {0: torch.export.Dim.DYNAMIC}}
)
print(ep)
```

## Invariants of torch.ops.higher_order.switch

There are several useful invariants for `torch.ops.higher_order.switch`:

- For index:

- If the index is a constant (e.g. a Python int), the operator may specialize to a single branch
- If the index is a tensor, it must be a single-element tensor
- Out-of-range indices are clamped to [0, len(branches)-1]
- For branches:

- All branches must have the same input and output signature
- The input and output signature will be a flattened tuple
- They are `torch.fx.GraphModule`
- Closures in original functions become explicit inputs. No closures.
- No mutations on inputs or globals are allowed
- Branch outputs must be tensors or possibly nested tuples/lists/dicts of tensors. Non-tensor leaves must be `int` or `None`. Diverging `int` values across branches are merged into a SymInt for dynamic shapes; `None` must match positionally across every branch.
- For operands:

- It will be a flat tuple of tensors
- Nesting of `torch.switch` in user program becomes nested graph modules

## API Reference

torch._higher_order_ops.switch.switch(*index*, *branches*, *operands=()*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_higher_order_ops/switch.py#L112)

Selects and runs one of N branch functions by index.

Warning

torch.switch is a prototype feature in PyTorch. It has limited support for input and
output types. Please look forward to a more stable implementation in a future version of
PyTorch. Read more about feature classification at:
[https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Equivalent to: `branches[index](*operands)` with index in `[0, len(branches))`.

Parameters:

- **index** (*Union**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - An int or single-element integer tensor
indicating which branch to run. Out-of-range values are clamped into
`[0, len(branches))`.
- **branches** (*Union**[*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Callable**,**...**]**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**Callable**]**]*) - Non-empty sequence of
callables. Each must accept operands and return the same structure of outputs.
- **operands** (*Tuple**of**possibly nested dict/list/tuple**of*[*torch.Tensor*](../tensors.html#torch.Tensor)) - Inputs to
the branch functions. Defaults to ().

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Restrictions:

- Each branch must have the same signature as operands and return the same
output structure (shape, dtype, etc.). Constant `int` and `None` leaves
are also permitted in branch outputs and are merged across branches (an
unbacked SymInt is introduced when `int` leaves differ between branches).
- Branches cannot have in-place mutations on inputs or global variables.