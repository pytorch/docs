# Control Flow - Scan

`torch.scan` is a structured control flow operator that performs an inclusive scan with a combine function.
It is commonly used for cumulative operations like cumsum, cumprod, or more general recurrences.
It can logically be seen as implemented as follows:

```
def scan(
 combine_fn: Callable[[PyTree, PyTree], tuple[PyTree, PyTree]],
 init: PyTree,
 xs: PyTree,
 *,
 dim: int = 0,
 reverse: bool = False,
) -> tuple[PyTree, PyTree]:
 carry = init
 ys = []
 for i in range(xs.size(dim)):
 x_slice = xs.select(dim, i)
 carry, y = combine_fn(carry, x_slice)
 ys.append(y)
 return carry, torch.stack(ys)
```

Warning

`torch.scan` is a prototype feature in PyTorch. You may run into miscompiles.
Read more about feature classification at:
https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

## Examples

Below is an example that uses scan to compute a cumulative sum:

```
import torch
from torch._higher_order_ops import scan

def add(carry: torch.Tensor, x: torch.Tensor):
 next_carry = carry + x
 y = next_carry.clone() # clone to avoid output-output aliasing
 return next_carry, y

init = torch.zeros(1)
xs = torch.arange(5, dtype=torch.float32)

final_carry, cumsum = scan(add, init=init, xs=xs)
print(final_carry)
print(cumsum)
```

We can export the model with scan for further transformations and deployment.
This example uses dynamic shapes to allow variable sequence length:

```
class ScanModule(torch.nn.Module):
 def forward(self, xs: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
 def combine_fn(carry, x):
 next_carry = carry + x
 return next_carry, next_carry.clone()

 init = torch.zeros_like(xs[0])
 return scan(combine_fn, init=init, xs=xs)

mod = ScanModule()
inp = torch.randn(5, 3)
ep = torch.export.export(mod, (inp,), dynamic_shapes={"xs": {0: torch.export.Dim.DYNAMIC}})
print(ep)
```

Notice that the combine function becomes a sub-graph attribute of the top-level graph module.

## Restrictions

- `combine_fn` must return tensors with the same metadata (shape, dtype) for `next_carry` as `init`.
- `combine_fn` must not in-place mutate its inputs. A clone before mutation is required.
- `combine_fn` must not mutate Python variables (e.g., list/dict) created outside the function.
- `combine_fn`'s output cannot alias any of the inputs. A clone is required.

## API Reference

torch._higher_order_ops.scan.scan(*combine_fn*, *init*, *xs*, ***, *dim=0*, *reverse=False*, *length=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/_higher_order_ops/scan.py#L109)

Performs an inclusive scan with a combine function.

Warning

`torch.scan` is a prototype feature in PyTorch. You may run into miscompiles.
Read more about feature classification at:
[https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Parameters:

- **combine_fn** (*Callable*) - A binary callable with type `(Tensor, Tensor) -> (Tensor, Tensor)`,
or if xs is a pytree `(pytree, pytree) -> (pytree, pytree)`.
The first input to `combine_fn` is the previous or initial scan carry
and the second input element to `combine_fn` is a slice of the input along dim.
The first output element of `combine_fn` is the next scan carry
and the second output of `combine_fn` represents a slice of the output.
This function must be pure, i.e., no lifted arguments are supported at the moment
and may not have any side effects.
- **init** ([*torch.Tensor*](../tensors.html#torch.Tensor)*or**pytree with tensor leaves*) - The initial scan carry, a tensor, or nested pytree of tensors.
The `init` is expected to have the same pytree structure as the first output element (i.e. carry)
of `combine_fn`.
- **xs** ([*torch.Tensor*](../tensors.html#torch.Tensor)*or**pytree with tensor leaves**or**None*) - The input tensor, or nested pytree of tensors.
May be `None` when `length` is provided, in which case `combine_fn` receives `None` as `x`
each step (counter-loop mode).

Keyword Arguments:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to scan over, default 0.
- **reverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - A boolean stating if the scan should be reversed with respect to `dim`, default `False`.
- **length** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*None*](https://docs.python.org/3/library/constants.html#None)) - Optional number of scan iterations, default `None`.
When `xs` has tensor leaves, `length` is optional; if given it must equal
`xs.shape[dim]` and serves only as a consistency check (no constraint when
`length` is `None`). When `xs` has no leaves (`None` or empty pytree),
`length` drives the number of iterations and `combine_fn` receives
`x=None` each step. `length=0` with no xs tensors is supported in
eager mode only; it is not supported under `torch.compile`.

Returns:

final_carry (torch.Tensor or pytree with tensor leaves),

the final carry of the scan operation with same pytree structure as init.

out (torch.Tensor or pytree with tensor leaves),

each tensor leaf is a stacked output along first dim, where each slice is the output of a scan iteration.
If the scan dimension has size 0, `final_carry` equals `init` unchanged and each output leaf has
size 0 along `dim`. The gradient of `final_carry` with respect to `init` is the identity
(not zero), since the body is never called and the carry passes through untouched.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

Restrictions:

- The combine_fn shouldn't have any aliasing between input-input, input-output, and output-output. E.g. return a view

or the same tensor as input is not supported. As a workaround, can clone the output to avoid aliasing.
- The combine_fn shouldn't mutate any inputs. We'll remove the mutation restriction for inference soon. Please file an issue

if you input mutation support for training is needed.
- The combine_fn's init carry should match the next_carry in pytree structure and in tensor metadata.

Example:

```
def add(x: torch.Tensor, y: torch.Tensor):
 next_carry = y = x + y
 # clone the output to avoid output-output aliasing
 return next_carry, y.clone()

i0 = torch.zeros(1)
xs = torch.arange(5)
# returns torch.tensor([10.]), torch.tensor([[0], [1.], [3.], [6.], [10.]])
last_carry, cumsum = scan(add, init=i0, xs=xs)
```