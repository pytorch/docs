# torch.compiler.load_cache_artifacts

torch.compiler.load_cache_artifacts(*serialized_artifacts*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/compiler/__init__.py#L772)

Hot loads cache artifacts that were previously serialized via
save_cache_artifacts

Example:

# From a previous invocation
artifacts = torch.compiler.save_cache_artifacts()

torch.compiler.load_cache_artifacts(artifacts[0])

Return type:

*CacheInfo* | None