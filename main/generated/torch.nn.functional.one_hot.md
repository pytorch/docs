# torch.nn.functional.one_hot

torch.nn.functional.one_hot(*tensor*, *num_classes=-1*) → LongTensor[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/nn/functional.py#L5699)

Takes LongTensor with index values of shape `(*)` and returns a tensor
of shape `(*, num_classes)` that have zeros everywhere except where the
index of last dimension matches the corresponding value of the input tensor,
in which case it will be 1.

See also [One-hot on Wikipedia](https://en.wikipedia.org/wiki/One-hot) .

Parameters:

- **tensor** (*LongTensor*) - class values of any shape.
- **num_classes** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Total number of classes. If set to -1, the number
of classes will be inferred as one greater than the largest class
value in the input tensor. Default: -1

Returns:

LongTensor that has one more dimension with 1 values at the
index of last dimension indicated by the input, and 0 everywhere
else.

Examples

```
>>> F.one_hot(torch.arange(0, 5) % 3)
tensor([[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1],
 [1, 0, 0],
 [0, 1, 0]])
>>> F.one_hot(torch.arange(0, 5) % 3, num_classes=5)
tensor([[1, 0, 0, 0, 0],
 [0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0],
 [1, 0, 0, 0, 0],
 [0, 1, 0, 0, 0]])
>>> F.one_hot(torch.arange(0, 6).view(3,2) % 3)
tensor([[[1, 0, 0],
 [0, 1, 0]],
 [[0, 0, 1],
 [1, 0, 0]],
 [[0, 1, 0],
 [0, 0, 1]]])
```