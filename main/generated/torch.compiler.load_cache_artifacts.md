# torch.compiler.load_cache_artifacts

torch.compiler.load_cache_artifacts(*serialized_artifacts*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/compiler/__init__.py#L651)

Hot loads cache artifacts that were previously serialized via
save_cache_artifacts

Example:

# From a previous invocation
artifacts = torch.compiler.save_cache_artifacts()

torch.compiler.load_cache_artifacts(artifacts[0])

Return type:

*CacheInfo* | None