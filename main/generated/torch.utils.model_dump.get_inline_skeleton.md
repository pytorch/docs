# torch.utils.model_dump.get_inline_skeleton

torch.utils.model_dump.get_inline_skeleton()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/utils/model_dump/__init__.py#L475)

Get a fully-inlined skeleton of the frontend.

The returned HTML page has no external network dependencies for code.
It can load model_info.json over HTTP, or be passed to burn_in_info.

Warning

`torch.utils.model_dump` is deprecated and unsafe on untrusted models:
inspecting a model can execute arbitrary code stored in it.