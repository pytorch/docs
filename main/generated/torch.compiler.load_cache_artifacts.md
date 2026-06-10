# torch.compiler.load_cache_artifacts

torch.compiler.load_cache_artifacts(*serialized_artifacts*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/compiler/__init__.py#L667)

Hot loads cache artifacts that were previously serialized via
save_cache_artifacts

Example:

# From a previous invocation
artifacts = torch.compiler.save_cache_artifacts()

torch.compiler.load_cache_artifacts(artifacts[0])

Return type:

*CacheInfo* | None