# torch.compiler.save_cache_artifacts

torch.compiler.save_cache_artifacts()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/compiler/__init__.py#L754)

Serializes all the cache artifacts that were created during the compilation

Example:

- Execute torch.compile
- Call torch.compiler.save_cache_artifacts()

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes), *CacheInfo*] | None