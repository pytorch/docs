# torch.utils.model_dump.get_inline_skeleton

torch.utils.model_dump.get_inline_skeleton()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/utils/model_dump/__init__.py#L386)

Get a fully-inlined skeleton of the frontend.

The returned HTML page has no external network dependencies for code.
It can load model_info.json over HTTP, or be passed to burn_in_info.