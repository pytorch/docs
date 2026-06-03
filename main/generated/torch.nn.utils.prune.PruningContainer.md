# PruningContainer

*class*torch.nn.utils.prune.PruningContainer(**args*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L269)

Container holding a sequence of pruning methods for iterative pruning.

Keeps track of the order in which pruning methods are applied and handles
combining successive pruning calls.

Accepts as argument an instance of a BasePruningMethod or an iterable of
them.

add_pruning_method(*method*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L293)

Add a child pruning `method` to the container.

Parameters:

**method** (*subclass**of*[*BasePruningMethod*](torch.nn.utils.prune.BasePruningMethod.html#torch.nn.utils.prune.BasePruningMethod)) - child pruning method
to be added to the container.

*classmethod*apply(*module*, *name*, **args*, *importance_scores=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L76)

Add pruning on the fly and reparameterization of a tensor.

Adds the forward pre-hook that enables pruning on the fly and
the reparameterization of a tensor in terms of the original tensor
and the pruning mask.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.
- **args** - arguments passed on to a subclass of
[`BasePruningMethod`](torch.nn.utils.prune.BasePruningMethod.html#torch.nn.utils.prune.BasePruningMethod)
- **importance_scores** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor of importance scores (of
same shape as module parameter) used to compute mask for pruning.
The values in this tensor indicate the importance of the
corresponding elements in the parameter being pruned.
If unspecified or None, the parameter will be used in its place.
- **kwargs** - keyword arguments passed on to a subclass of a
[`BasePruningMethod`](torch.nn.utils.prune.BasePruningMethod.html#torch.nn.utils.prune.BasePruningMethod)

apply_mask(*module*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L53)

Simply handles the multiplication between the parameter being pruned and the generated mask.

Fetches the mask and the original tensor from the module
and returns the pruned version of the tensor.

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune

Returns:

pruned version of the input tensor

Return type:

pruned_tensor ([torch.Tensor](../tensors.html#torch.Tensor))

compute_mask(*t*, *default_mask*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L321)

Apply the latest `method` by computing the new partial masks and returning its combination with the `default_mask`.

The new partial mask should be computed on the entries or channels
that were not zeroed out by the `default_mask`.
Which portions of the tensor `t` the new mask will be calculated from
depends on the `PRUNING_TYPE` (handled by the type handler):

- for 'unstructured', the mask will be computed from the raveled
list of nonmasked entries;
- for 'structured', the mask will be computed from the nonmasked
channels in the tensor;
- for 'global', the mask will be computed across all entries.

Parameters:

- **t** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor representing the parameter to prune
(of same dimensions as `default_mask`).
- **default_mask** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - mask from previous pruning iteration.

Returns:

new mask that combines the effects
of the `default_mask` and the new mask from the current
pruning `method` (of same dimensions as `default_mask` and
`t`).

Return type:

mask ([torch.Tensor](../tensors.html#torch.Tensor))

prune(*t*, *default_mask=None*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L208)

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

remove(*module*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/utils/prune.py#L240)

Remove the pruning reparameterization from a module.

The pruned parameter named `name` remains permanently pruned,
and the parameter named `name+'_orig'` is removed from the parameter list.
Similarly, the buffer named `name+'_mask'` is removed from the buffers.

Note

Pruning itself is NOT undone or reversed!