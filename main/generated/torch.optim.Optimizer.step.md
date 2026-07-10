# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/library/constants.html#None) = None*) → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L1093)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/library/functions.html#float)]*) → [float](https://docs.python.org/3/library/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.