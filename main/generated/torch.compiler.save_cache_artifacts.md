# torch.compiler.save_cache_artifacts

torch.compiler.save_cache_artifacts()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/compiler/__init__.py#L792)

Serializes all the cache artifacts that were created during the compilation

Example:

- Execute torch.compile
- Call torch.compiler.save_cache_artifacts()

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes), *CacheInfo*] | None