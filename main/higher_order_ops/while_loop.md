# Control Flow - While Loop

`torch.while_loop` is a structured control flow operator that runs a body function while a condition is true.
It can logically be seen as implemented as follows:

```
def while_loop(
 cond_fn: Callable[..., bool],
 body_fn: Callable[..., tuple],
 carried_inputs: tuple,
):
 val = carried_inputs
 while cond_fn(*val):
 val = body_fn(*val)
 return val
```

Warning

`torch.while_loop` is a prototype feature in PyTorch. It has limited support for input and output types.
Please look forward to a more stable implementation in a future version of PyTorch.
Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

## Examples

Below is a basic example that uses while_loop to iterate until a condition is met:

```
import torch
from torch._higher_order_ops import while_loop

class M(torch.nn.Module):

 def cond_fn(self, iter_count, x):
 return iter_count.sum() > 0

 def body_fn(self, iter_count, x):
 return iter_count - 1, x * 2

 def forward(self, init_iter, init_x):
 final_iter, final_x = while_loop(self.cond_fn, self.body_fn, (init_iter, init_x))
 return final_iter, final_x

m = M()
```

We can eagerly run the model and expect the results vary based on input shape:

```
_, final_x = m(torch.tensor([3]), torch.ones(3))
assert torch.equal(final_x, torch.ones(3) * 2**3)

_, final_x = m(torch.tensor([10]), torch.ones(3))
assert torch.equal(final_x, torch.ones(3) * 2**10)
```

We can export the model for further transformations and deployment. This gives us an exported program that preserves the while_loop structure:

```
ep = torch.export.export(M(), (torch.tensor([10]), torch.ones(3)))
print(ep)
```

Notice that both the condition and body functions become sub-graph attributes of
the top-level graph module.

## Restrictions

- `body_fn` must return tensors or integers with the same metadata (shape, dtype) as inputs.
- `body_fn` and `cond_fn` must not in-place mutate the `carried_inputs`. A clone before mutation is required.
- `body_fn` and `cond_fn` must not mutate Python variables (e.g., list/dict) created outside the function.
- `body_fn` and `cond_fn`'s output cannot alias any of the inputs. A clone is required.

## API Reference

torch._higher_order_ops.while_loop.while_loop(*cond_fn*, *body_fn*, *carried_inputs*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/_higher_order_ops/while_loop.py#L136)

Run `body_fn(*carried_inputs)` while `cond_fn(*carried_inputs)` returns
a True scalar tensor. Returns the output of body_fn or initial
carried_inputs.

Warning

torch.while_loop is a prototype feature in PyTorch. It has limited support for input and output types and
doesn't support training currently. Please look forward to a more stable implementation in a future version of PyTorch.
Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

while_loop is a structured control flow operator. It preserves the loop semantic across the torch.compile and torch.export.

while_loop is equivalent to the following:

```
def while_loop(cond_fn, body_fn, carried_inputs):
 val = carried_inputs
 while cond_fn(*val):
 val = body_fn(*val)
 return val
```

Parameters:

- **cond_fn** (*Callable*) - A callable function that returns a boolean Scalar tensor or a python boolean.
- **body_fn** (*Callable*) - A callable function that takes the same inputs as cond_fn and returns a tuple of tensors or ints
- **carried_inputs** (*Tuple**of**possibly nested dict/list/tuple**of**tensors**or**ints*) - A tuple of inputs to cond_fn and body_fn.
It's also the initial value of states that are carried across iterations. Note that when pass an integer as carry,
the corresponding return of while_loop will be another int with unknown values because we don't know how many
iterations while_loop will run.

Example 1:

```
def cond_fn(iter, x):
 return iter.sum() < 10

def body_fn(iter, x):
 return iter + 1, x.sin()

while_loop(cond_fn, body_fn, (torch.zeros(1), torch.randn(3, 4)))
```

Example 2:

```
def cond_fn(int_iter, x):
 return 2 * int_iter < x.shape[0]

def body_fn(int_iter, x):
 return int_iter + 1, x + int_iter

while_loop(cond_fn, body_fn, (0, torch.randn(3, 4)))
```

Restrictions:

> - body_fn must return tensors or int with the same metadata (e.g.shape, dtype) as inputs.
> - body_fn and cond_fn must not in-place mutate the carried_inputs. A clone before the mutation is required.
> - body_fn and cond_fn must not mutate python variables (e.g. list/dict) created outside of the body_fn.
> - body_fn and cond_fn's output cannot alias any of the inputs. A clone is required.
> - During inference, body_fn and cond_fn can in-place mutate tensors that are not
> carried_inputs, such as module buffers and captured tensors from the enclosing scope.