# torch.compiler.load_cache_artifacts

torch.compiler.load_cache_artifacts(*serialized_artifacts*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/compiler/__init__.py#L773)

Hot loads cache artifacts that were previously serialized via
save_cache_artifacts

Example:

# From a previous invocation
artifacts = torch.compiler.save_cache_artifacts()

torch.compiler.load_cache_artifacts(artifacts[0])

Return type:

*CacheInfo* | None