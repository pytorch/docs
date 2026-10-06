# torch.compiler.save_cache_artifacts

torch.compiler.save_cache_artifacts()[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/compiler/__init__.py#L754)

Serializes all the cache artifacts that were created during the compilation

Example:

- Execute torch.compile
- Call torch.compiler.save_cache_artifacts()

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes), *CacheInfo*] | None