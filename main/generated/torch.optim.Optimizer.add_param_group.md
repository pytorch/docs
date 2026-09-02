# torch.optim.Optimizer.add_param_group

Optimizer.add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/optim/optimizer.py#L1136)

Add a param group to the [`Optimizer`](../optim.html#torch.optim.Optimizer) s param_groups.

This can be useful when fine tuning a pre-trained network as frozen layers can be made
trainable and added to the [`Optimizer`](../optim.html#torch.optim.Optimizer) as training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Specifies what Tensors should be optimized along with group
specific optimization options.