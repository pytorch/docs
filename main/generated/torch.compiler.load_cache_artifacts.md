# torch.compiler.load_cache_artifacts

torch.compiler.load_cache_artifacts(*serialized_artifacts*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L772)

Hot loads cache artifacts that were previously serialized via
save_cache_artifacts

Example:

# From a previous invocation
artifacts = torch.compiler.save_cache_artifacts()

torch.compiler.load_cache_artifacts(artifacts[0])

Return type:

*CacheInfo* | None