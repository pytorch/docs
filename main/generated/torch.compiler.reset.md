# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/compiler/__init__.py#L80)

Reset the in-process compiler state.

This function clears Dynamo's in-memory compilation caches and related
process-local state used by [`torch.compile()`](torch.compile.html#torch.compile). It does not delete
filesystem caches, such as Inductor's disk cache.