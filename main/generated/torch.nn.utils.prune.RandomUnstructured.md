# RandomUnstructured

*class*torch.nn.utils.prune.RandomUnstructured(*amount*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/nn/utils/prune.py#L444)

Prune (currently unpruned) units in a tensor at random.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.
- **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - quantity of parameters to prune.
If `float`, should be between 0.0 and 1.0 and represent the
fraction of parameters to prune. If `int`, it represents the
absolute number of parameters to prune.

*classmethod*apply(*module*, *name*, *amount*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/nn/utils/prune.py#L483)

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

apply_mask(*module*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/nn/utils/prune.py#L53)

Simply handles the multiplication between the parameter being pruned and the generated mask.

Fetches the mask and the original tensor from the module
and returns the pruned version of the tensor.

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune

Returns:

pruned version of the input tensor

Return type:

pruned_tensor ([torch.Tensor](../tensors.html#torch.Tensor))

prune(*t*, *default_mask=None*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/nn/utils/prune.py#L208)

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

remove(*module*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/nn/utils/prune.py#L240)

Remove the pruning reparameterization from a module.

The pruned parameter named `name` remains permanently pruned,
and the parameter named `name+'_orig'` is removed from the parameter list.
Similarly, the buffer named `name+'_mask'` is removed from the buffers.

Note

Pruning itself is NOT undone or reversed!