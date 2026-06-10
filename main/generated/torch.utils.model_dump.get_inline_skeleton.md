# torch.utils.model_dump.get_inline_skeleton

torch.utils.model_dump.get_inline_skeleton()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/utils/model_dump/__init__.py#L386)

Get a fully-inlined skeleton of the frontend.

The returned HTML page has no external network dependencies for code.
It can load model_info.json over HTTP, or be passed to burn_in_info.