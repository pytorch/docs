# LnStructured

*class*torch.nn.utils.prune.LnStructured(*amount*, *n*, *dim=-1*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L675)

Prune entire (currently unpruned) channels in a tensor based on their L`n`-norm.

Parameters:

- **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - quantity of channels to prune.
If `float`, should be between 0.0 and 1.0 and represent the
fraction of parameters to prune. If `int`, it represents the
absolute number of parameters to prune.
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,**inf**,**-inf**,**'fro'**,**'nuc'*) - See documentation of valid
entries for argument `p` in [`torch.norm()`](torch.norm.html#torch.norm).
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - index of the dim along which we define
channels to prune. Default: -1.

*classmethod*apply(*module*, *name*, *amount*, *n*, *dim*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L769)

Add pruning on the fly and reparameterization of a tensor.

Adds the forward pre-hook that enables pruning on the fly and
the reparameterization of a tensor in terms of the original tensor
and the pruning mask.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.
- **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - quantity of parameters to prune.
If `float`, should be between 0.0 and 1.0 and represent the
fraction of parameters to prune. If `int`, it represents the
absolute number of parameters to prune.
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,**inf**,**-inf**,**'fro'**,**'nuc'*) - See documentation of valid
entries for argument `p` in [`torch.norm()`](torch.norm.html#torch.norm).
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - index of the dim along which we define channels to
prune.
- **importance_scores** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor of importance scores (of same
shape as module parameter) used to compute mask for pruning.
The values in this tensor indicate the importance of the corresponding
elements in the parameter being pruned.
If unspecified or None, the module parameter will be used in its place.

apply_mask(*module*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L53)

Simply handles the multiplication between the parameter being pruned and the generated mask.

Fetches the mask and the original tensor from the module
and returns the pruned version of the tensor.

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune

Returns:

pruned version of the input tensor

Return type:

pruned_tensor ([torch.Tensor](../tensors.html#torch.Tensor))

compute_mask(*t*, *default_mask*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L698)

Compute and returns a mask for the input tensor `t`.

Starting from a base `default_mask` (which should be a mask of ones
if the tensor has not been pruned yet), generate a mask to apply on
top of the `default_mask` by zeroing out the channels along the
specified dim with the lowest L`n`-norm.

Parameters:

- **t** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor representing the parameter to prune
- **default_mask** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - Base mask from previous pruning
iterations, that need to be respected after the new mask is
applied. Same dims as `t`.

Returns:

mask to apply to `t`, of same dims as `t`

Return type:

mask ([torch.Tensor](../tensors.html#torch.Tensor))

Raises:

[**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError) - if `self.dim >= len(t.shape)`

prune(*t*, *default_mask=None*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L208)

Compute and returns a pruned version of input tensor `t`.

According to the pruning rule specified in `compute_mask()`.

Parameters:

- **t** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor to prune (of same dimensions as
`default_mask`).
- **importance_scores** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor of importance scores (of
same shape as `t`) used to compute mask for pruning `t`.
The values in this tensor indicate the importance of the
corresponding elements in the `t` that is being pruned.
If unspecified or None, the tensor `t` will be used in its place.
- **default_mask** ([*torch.Tensor*](../tensors.html#torch.Tensor)*,**optional*) - mask from previous pruning
iteration, if any. To be considered when determining what
portion of the tensor that pruning should act on. If None,
default to a mask of ones.

Returns:

pruned version of tensor `t`.

remove(*module*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/prune.py#L240)

Remove the pruning reparameterization from a module.

The pruned parameter named `name` remains permanently pruned,
and the parameter named `name+'_orig'` is removed from the parameter list.
Similarly, the buffer named `name+'_mask'` is removed from the buffers.

Note

Pruning itself is NOT undone or reversed!