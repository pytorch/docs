# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/compiler/__init__.py#L81)

Reset the in-process compiler state.

This function clears Dynamo's in-memory compilation caches and related
process-local state used by [`torch.compile()`](torch.compile.html#torch.compile). It does not delete
filesystem caches, such as Inductor's disk cache.