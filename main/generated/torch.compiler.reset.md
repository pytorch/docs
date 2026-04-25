# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/compiler/__init__.py#L60)

This function clears all compilation caches and restores the system to its initial state.
It is recommended to call this function, especially after using operations like torch.compile(...)
to ensure a clean state before another unrelated compilation