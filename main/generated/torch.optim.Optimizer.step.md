# torch.optim.Optimizer.step

Optimizer.step(*closure: [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/optim/optimizer.py#L1178)

Optimizer.step(*closure: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [float](https://docs.python.org/3/builtins/functions.html#float)]*) → [float](https://docs.python.org/3/builtins/functions.html#float)

Perform a single optimization step to update parameter.

Parameters:

**closure** (*Callable*) - A closure that reevaluates the model and
returns the loss. Optional for most optimizers.