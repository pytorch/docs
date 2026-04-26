# Control Flow - Map

`torch.map` is a structured control flow operator that applies a function over the leading dimension of
input tensors. It can logically be seen as implemented as follows:

```
def map(
 f: Callable[[PyTree, ...], PyTree],
 xs: Union[PyTree, torch.Tensor],
 *args,
):
 out = []
 for idx in range(xs.size(0)):
 xs_sliced = xs.select(0, idx)
 out.append(f(xs_sliced, *args))
 return torch.stack(out)
```

Warning

`torch._higher_order_ops.map` is a prototype feature in PyTorch. You may run into miscompiles.
Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

## Examples

Below is an example that uses map to apply a function over a batch:

```
import torch
from torch._higher_order_ops import map

def f(x):
 return x.sin() + x.cos()

xs = torch.randn(3, 4, 5) # batch of 3 tensors, each 4x5
# Applies f to each of the 3 slices
result = map(f, xs) # returns tensor of shape [3, 4, 5]
print(result)
```

We can export the model with map for further transformations and deployment.
This example uses dynamic shapes to allow variable batch size:

```
class MapModule(torch.nn.Module):
 def __init__(self):
 super().__init__()

 def forward(self, xs: torch.Tensor) -> torch.Tensor:
 def body_fn(x):
 return x.sin() + x.cos()

 return map(body_fn, xs)

mod = MapModule()
inp = torch.randn(3, 4)
ep = torch.export.export(mod, (inp,), dynamic_shapes={"xs": {0: torch.export.Dim.DYNAMIC}})
print(ep)
```

Notice that `torch.map` is lowered to `torch.ops.higher_order.map_impl`, and the body function becomes a
sub-graph attribute of the top-level graph module.

## Restrictions

- Mapped `xs` can only consist of tensors.
- Leading dimensions of all tensors in `xs` must be consistent and non-zero.
- The body function must not mutate inputs.

## API Reference

torch._higher_order_ops.map.map(*f*, *xs*, **args*)[[source]](https://github.com/pytorch/pytorch/blob/dff44973f3eba04a92de8499c17cd237997140f2/torch/_higher_order_ops/map.py#L47)

Performs a map of f with xs. Intuitively, you can think of the semantic being:

```
out = []
for idx in len(xs.size(0)):
 xs_sliced = xs.select(0, idx)
 out.append(f(xs_sliced, *args))
torch.stack(out)
```

Warning

`torch._higher_order_ops.map` is a prototype feature in PyTorch. It currently
does not support autograd and you may run into miscompiles.
Read more about feature classification at:
[https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Parameters:

- **f** (*Callable*) - a callable that takes an input x, that could either be a single Tensor
or a nested dict, list of tensors and some additional inputs
- **xs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|*[*Tensor*](../tensors.html#torch.Tensor)) - the inputs that're to be mapped over. We'll iterate over the first dim of each x
and perform f on each slice.
- ***args** (*TypeVarTuple*) - additional arguments provided to each step of f. They could also be omitted and
map is able to automatically figure out the read dependency.

Returns:

the stacked output for each step of f

Example:

```
def f(xs):
 return xs[0] + xs[1] + const1 + const2

xs = [torch.randn(2, 3), torch.randn(2, 3)]
const1 = torch.randn(2, 3)
const2 = torch.randn(2, 3)
# returns a tensor of shape [2, 2, 3]
torch._higher_order_ops.map(f, xs)
```