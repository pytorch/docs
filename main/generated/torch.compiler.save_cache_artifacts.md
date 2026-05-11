# torch.compiler.save_cache_artifacts

torch.compiler.save_cache_artifacts()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/compiler/__init__.py#L632)

Serializes all the cache artifacts that were created during the compilation

Example:

- Execute torch.compile
- Call torch.compiler.save_cache_artifacts()

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes), *CacheInfo*] | None