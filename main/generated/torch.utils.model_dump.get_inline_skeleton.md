# torch.utils.model_dump.get_inline_skeleton

torch.utils.model_dump.get_inline_skeleton()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/utils/model_dump/__init__.py#L386)

Get a fully-inlined skeleton of the frontend.

The returned HTML page has no external network dependencies for code.
It can load model_info.json over HTTP, or be passed to burn_in_info.