# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L81)

Reset the in-process compiler state.

This function clears Dynamo's in-memory compilation caches and related
process-local state used by [`torch.compile()`](torch.compile.html#torch.compile). It does not delete
filesystem caches, such as Inductor's disk cache.