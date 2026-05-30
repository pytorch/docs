# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/compiler/__init__.py#L60)

This function clears all compilation caches and restores the system to its initial state.
It is recommended to call this function, especially after using operations like torch.compile(...)
to ensure a clean state before another unrelated compilation