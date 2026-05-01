# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/compiler/__init__.py#L60)

This function clears all compilation caches and restores the system to its initial state.
It is recommended to call this function, especially after using operations like torch.compile(...)
to ensure a clean state before another unrelated compilation