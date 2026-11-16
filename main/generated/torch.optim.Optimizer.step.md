# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/optim/optimizer.py#L1178)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/builtins/functions.html#float)]*) → [float](https://docs.python.org/3/builtins/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.