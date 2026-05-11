# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/compiler/__init__.py#L60)

This function clears all compilation caches and restores the system to its initial state.
It is recommended to call this function, especially after using operations like torch.compile(...)
to ensure a clean state before another unrelated compilation