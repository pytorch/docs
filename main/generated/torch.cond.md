# torch.cond

torch.cond(*pred*, *true_fn*, *false_fn*, *operands=()*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/_higher_order_ops/cond.py#L95)

Conditionally applies true_fn or false_fn.

Warning

torch.cond is a prototype feature in PyTorch. It has limited support for input and output types.
Please look forward to a more stable implementation in a future version of PyTorch.
Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

cond is structured control flow operator. That is, it is like a Python if-statement,
but has restrictions on true_fn, false_fn, and operands that enable it to be
capturable using torch.compile and torch.export.

Assuming the constraints on cond's arguments are met, cond is equivalent to the following:

```
def cond(pred, true_branch, false_branch, operands):
 if pred:
 return true_branch(*operands)
 else:
 return false_branch(*operands)
```

Parameters:

- **pred** (*Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - A boolean expression or a tensor with one element,
indicating which branch function to apply.
- **true_fn** (*Callable*) - A callable function (a -> b) that is within the
scope that is being traced.
- **false_fn** (*Callable*) - A callable function (a -> b) that is within the
scope that is being traced. The true branch and false branch must
have consistent input and outputs, meaning the inputs have to be
the same, and the outputs have to be the same type and shape. Int
output is also allowed. We'll make the output dynamic by turning it
into a symint.
- **operands** (*Tuple**of**possibly nested dict/list/tuple**of*[*torch.Tensor*](../tensors.html#torch.Tensor)) - A tuple of inputs to the
true/false functions. It can be empty if true_fn/false_fn doesn't require input. Defaults to ().

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Example:

```
def true_fn(x: torch.Tensor):
 return x.cos()

def false_fn(x: torch.Tensor):
 return x.sin()

return cond(x.shape[0] > 4, true_fn, false_fn, (x,))
```

Restrictions:

- The conditional statement (aka pred) must meet one of the following constraints:

- It's a torch.Tensor with only one element, and torch.bool dtype
- It's a boolean expression, e.g. x.shape[0] > 10 or x.dim() > 1 and x.shape[1] > 10
- The branch function (aka true_fn/false_fn) must meet all of the following constraints:

- The function signature must match with operands.
- The function must return a tensor with the same metadata, e.g. shape,
dtype, etc.
- The function cannot have in-place mutations on global variables.
(Note: in-place tensor operations such as add_ for intermediate results
are allowed in a branch)
- The function can perform in-place mutations on its input tensors during inference (i.e.,
when torch.is_grad_enabled() is False).
Note: When using torch.compile() with a non-constant predicate, the outputs will always
be new tensors that do not share object identity with the original inputs.

Example:

```
def true_fn(x):
 return x.sin_()

def false_fn(x):
 return x + 1

def f(x):
 return cond(x.sum() > 0, true_fn, false_fn, (x,))

x = torch.ones(4)
with torch.no_grad():
 result = torch.compile(f)(x)
assert result is not x # result is a new tensor, not the original x
```