# torch.utils.model_dump.get_inline_skeleton

torch.utils.model_dump.get_inline_skeleton()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/utils/model_dump/__init__.py#L386)

Get a fully-inlined skeleton of the frontend.

The returned HTML page has no external network dependencies for code.
It can load model_info.json over HTTP, or be passed to burn_in_info.