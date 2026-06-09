# BasePruningMethod

*class*torch.nn.utils.prune.BasePruningMethod[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L11)

Abstract base class for creation of new pruning techniques.

Provides a skeleton for customization requiring the overriding of methods
such as `compute_mask()` and `apply()`.

*classmethod*apply(*module*, *name*, **args*, *importance_scores=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L76)

Add pruning on the fly and reparameterization of a tensor.

Adds the forward pre-hook that enables pruning on the fly and
the reparameterization of a tensor in terms of the original tensor
and the pruning mask.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.
- **args** - arguments passed on to a subclass of
`BasePruningMethod`
- **importance_scores** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor of importance scores (of
same shape as module parameter) used to compute mask for pruning.
The values in this tensor indicate the importance of the
corresponding elements in the parameter being pruned.
If unspecified or None, the parameter will be used in its place.
- **kwargs** - keyword arguments passed on to a subclass of a
`BasePruningMethod`

apply_mask(*module*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L53)

Simply handles the multiplication between the parameter being pruned and the generated mask.

Fetches the mask and the original tensor from the module
and returns the pruned version of the tensor.

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune

Returns:

pruned version of the input tensor

Return type:

pruned_tensor ([torch.Tensor](../tensors.html#torch.Tensor))

*abstract*compute_mask(*t*, *default_mask*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L33)

Compute and returns a mask for the input tensor `t`.

Starting from a base `default_mask` (which should be a mask of ones
if the tensor has not been pruned yet), generate a random mask to
apply on top of the `default_mask` according to the specific pruning
method recipe.

Parameters:

- **t** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor representing the importance scores of the
- **prune.** (*parameter to*) -
- **default_mask** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - Base mask from previous pruning
- **iterations** -
- **is** (*that need to be respected after the new mask*) -
- **t.** (*applied. Same dims as*) -

Returns:

mask to apply to `t`, of same dims as `t`

Return type:

mask ([torch.Tensor](../tensors.html#torch.Tensor))

prune(*t*, *default_mask=None*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L208)

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

remove(*module*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/nn/utils/prune.py#L240)

Remove the pruning reparameterization from a module.

The pruned parameter named `name` remains permanently pruned,
and the parameter named `name+'_orig'` is removed from the parameter list.
Similarly, the buffer named `name+'_mask'` is removed from the buffers.

Note

Pruning itself is NOT undone or reversed!