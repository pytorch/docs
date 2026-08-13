# torch.optim.Optimizer.add_param_group

Optimizer.add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/optim/optimizer.py#L1126)

Add a param group to the [`Optimizer`](../optim.html#torch.optim.Optimizer) s param_groups.

This can be useful when fine tuning a pre-trained network as frozen layers can be made
trainable and added to the [`Optimizer`](../optim.html#torch.optim.Optimizer) as training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Specifies what Tensors should be optimized along with group
specific optimization options.