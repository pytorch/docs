# Tensor Views

PyTorch allows a tensor to be a `View` of an existing tensor. View tensor shares the same underlying data
with its base tensor. Supporting `View` avoids explicit data copy, thus allows us to do fast and memory efficient
reshaping, slicing and element-wise operations.

For example, to get a view of an existing tensor `t`, you can call `t.view(...)`.

```
>>> t = torch.rand(4, 4)
>>> b = t.view(2, 8)
>>> t.storage().data_ptr() == b.storage().data_ptr() # `t` and `b` share the same underlying data.
True
# Modifying view tensor changes base tensor as well.
>>> b[0][0] = 3.14
>>> t[0][0]
tensor(3.14)
```

Since views share underlying data with its base tensor, if you edit the data
in the view, it will be reflected in the base tensor as well.

Typically a PyTorch op returns a new tensor as output, e.g. [`add()`](generated/torch.Tensor.add.html#torch.Tensor.add).
But in case of view ops, outputs are views of input tensors to avoid unnecessary data copy.
No data movement occurs when creating a view, view tensor just changes the way
it interprets the same data. Taking a view of contiguous tensor could potentially produce a non-contiguous tensor.
Users should pay additional attention as contiguity might have implicit performance impact.
[`transpose()`](generated/torch.Tensor.transpose.html#torch.Tensor.transpose) is a common example.

```
>>> base = torch.tensor([[0, 1],[2, 3]])
>>> base.is_contiguous()
True
>>> t = base.transpose(0, 1) # `t` is a view of `base`. No data movement happened here.
# View tensors might be non-contiguous.
>>> t.is_contiguous()
False
# To get a contiguous tensor, call `.contiguous()` to enforce
# copying data when `t` is not contiguous.
>>> c = t.contiguous()
```

For reference, here's a full list of view ops in PyTorch:

- Basic slicing and indexing op, e.g. `tensor[0, 2:, 1:7:2]` returns a view of base `tensor`, see note below.
- [`adjoint()`](generated/torch.Tensor.adjoint.html#torch.Tensor.adjoint)
- [`as_strided()`](generated/torch.Tensor.as_strided.html#torch.Tensor.as_strided)
- [`detach()`](generated/torch.Tensor.detach.html#torch.Tensor.detach)
- [`diagonal()`](generated/torch.Tensor.diagonal.html#torch.Tensor.diagonal)
- [`expand()`](generated/torch.Tensor.expand.html#torch.Tensor.expand)
- [`expand_as()`](generated/torch.Tensor.expand_as.html#torch.Tensor.expand_as)
- [`movedim()`](generated/torch.Tensor.movedim.html#torch.Tensor.movedim)
- [`narrow()`](generated/torch.Tensor.narrow.html#torch.Tensor.narrow)
- [`permute()`](generated/torch.Tensor.permute.html#torch.Tensor.permute)
- [`select()`](generated/torch.Tensor.select.html#torch.Tensor.select)
- [`squeeze()`](generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze)
- [`transpose()`](generated/torch.Tensor.transpose.html#torch.Tensor.transpose)
- [`t()`](generated/torch.Tensor.t.html#torch.Tensor.t)
- [`T`](tensors.html#torch.Tensor.T)
- [`H`](tensors.html#torch.Tensor.H)
- [`mT`](tensors.html#torch.Tensor.mT)
- [`mH`](tensors.html#torch.Tensor.mH)
- [`real`](generated/torch.Tensor.real.html#torch.Tensor.real)
- [`imag`](generated/torch.Tensor.imag.html#torch.Tensor.imag)
- `view_as_real()`
- [`unflatten()`](generated/torch.Tensor.unflatten.html#torch.Tensor.unflatten)
- [`unfold()`](generated/torch.Tensor.unfold.html#torch.Tensor.unfold)
- [`unsqueeze()`](generated/torch.Tensor.unsqueeze.html#torch.Tensor.unsqueeze)
- [`view()`](generated/torch.Tensor.view.html#torch.Tensor.view)
- [`view_as()`](generated/torch.Tensor.view_as.html#torch.Tensor.view_as)
- [`unbind()`](generated/torch.Tensor.unbind.html#torch.Tensor.unbind)
- [`split()`](generated/torch.Tensor.split.html#torch.Tensor.split)
- [`hsplit()`](generated/torch.Tensor.hsplit.html#torch.Tensor.hsplit)
- [`vsplit()`](generated/torch.Tensor.vsplit.html#torch.Tensor.vsplit)
- [`tensor_split()`](generated/torch.Tensor.tensor_split.html#torch.Tensor.tensor_split)
- `split_with_sizes()`
- [`swapaxes()`](generated/torch.Tensor.swapaxes.html#torch.Tensor.swapaxes)
- [`swapdims()`](generated/torch.Tensor.swapdims.html#torch.Tensor.swapdims)
- [`chunk()`](generated/torch.Tensor.chunk.html#torch.Tensor.chunk)
- [`indices()`](generated/torch.Tensor.indices.html#torch.Tensor.indices) (sparse tensor only)
- [`values()`](generated/torch.Tensor.values.html#torch.Tensor.values) (sparse tensor only)

Note

When accessing the contents of a tensor via indexing, PyTorch follows Numpy behaviors
that basic indexing returns views, while advanced indexing returns a copy.
Assignment via either basic or advanced indexing is in-place. See more examples in
[Numpy indexing documentation](https://numpy.org/doc/stable/user/basics.indexing.html).

It's also worth mentioning a few ops with special behaviors:

- [`reshape()`](generated/torch.Tensor.reshape.html#torch.Tensor.reshape), [`reshape_as()`](generated/torch.Tensor.reshape_as.html#torch.Tensor.reshape_as) and [`flatten()`](generated/torch.Tensor.flatten.html#torch.Tensor.flatten) can return either a view or new tensor, user code shouldn't rely on whether it's view or not.
- [`contiguous()`](generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous) returns **itself** if input tensor is already contiguous, otherwise it returns a new contiguous tensor by copying data.

For a more detailed walk-through of PyTorch internal implementation,
please refer to [ezyang's blogpost about PyTorch Internals](http://blog.ezyang.com/2019/05/pytorch-internals/).