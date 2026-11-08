# torch.compiler.reset

torch.compiler.reset()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/compiler/__init__.py#L82)

Reset the in-process compiler state.

This function clears Dynamo's in-memory compilation caches and related
process-local state used by [`torch.compile()`](torch.compile.html#torch.compile). It does not delete
filesystem caches, such as Inductor's disk cache.