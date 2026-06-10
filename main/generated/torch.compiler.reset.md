# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/compiler/__init__.py#L60)

Reset the in-process compiler state.

This function clears Dynamo's in-memory compilation caches and related
process-local state used by [`torch.compile()`](torch.compile.html#torch.compile). It does not delete
filesystem caches, such as Inductor's disk cache.