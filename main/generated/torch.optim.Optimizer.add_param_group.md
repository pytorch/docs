# torch.optim.Optimizer.add_param_group

Optimizer.add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/optim/optimizer.py#L1126)

Add a param group to the [`Optimizer`](../optim.html#torch.optim.Optimizer) s param_groups.

This can be useful when fine tuning a pre-trained network as frozen layers can be made
trainable and added to the [`Optimizer`](../optim.html#torch.optim.Optimizer) as training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Specifies what Tensors should be optimized along with group
specific optimization options.