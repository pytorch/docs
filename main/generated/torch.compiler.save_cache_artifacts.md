# torch.compiler.save_cache_artifacts

torch.compiler.save_cache_artifacts()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/compiler/__init__.py#L739)

Serializes all the cache artifacts that were created during the compilation

Example:

- Execute torch.compile
- Call torch.compiler.save_cache_artifacts()

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes), *CacheInfo*] | None