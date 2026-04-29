# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/library/constants.html#None) = None*) → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/optim/optimizer.py#L1094)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/library/functions.html#float)]*) → [float](https://docs.python.org/3/library/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.