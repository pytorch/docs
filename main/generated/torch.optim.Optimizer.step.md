# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/optim/optimizer.py#L1135)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/builtins/functions.html#float)]*) → [float](https://docs.python.org/3/builtins/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.