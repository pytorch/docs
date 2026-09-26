# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/optim/optimizer.py#L1127)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/builtins/functions.html#float)]*) → [float](https://docs.python.org/3/builtins/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.