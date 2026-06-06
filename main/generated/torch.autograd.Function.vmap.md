# torch.autograd.Function.vmap

*static*Function.vmap(*info*, *in_dims*, **args*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/autograd/function.py#L576)

Define the behavior for this autograd.Function underneath [`torch.vmap()`](torch.vmap.html#torch.vmap).

For a [`torch.autograd.Function()`](../autograd.html#torch.autograd.Function) to support
[`torch.vmap()`](torch.vmap.html#torch.vmap), you must either override this static method, or set
`generate_vmap_rule` to `True` (you may not do both).

If you choose to override this staticmethod: it must accept

- an `info` object as the first argument. `info.batch_size`
specifies the size of the dimension being vmapped over,
while `info.randomness` is the randomness option passed to
[`torch.vmap()`](torch.vmap.html#torch.vmap).
- an `in_dims` tuple as the second argument.
For each arg in `args`, `in_dims` has a corresponding
`Optional[int]`. It is `None` if the arg is not a Tensor or if
the arg is not being vmapped over, otherwise, it is an integer
specifying what dimension of the Tensor is being vmapped over.
- `*args`, which is the same as the args to [`forward()`](torch.autograd.Function.forward.html#torch.autograd.Function.forward).

The return of the vmap staticmethod is a tuple of `(output, out_dims)`.
Similar to `in_dims`, `out_dims` should be of the same structure as
`output` and contain one `out_dim` per output that specifies if the
output has the vmapped dimension and what index it is in.

Please see [Extending torch.func with autograd.Function](../notes/extending.func.html#func-autograd-function) for more details.