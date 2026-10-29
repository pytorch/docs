# torch.utils.model_dump.get_model_info

torch.utils.model_dump.get_model_info(*path_or_file*, *title=None*, *extra_file_size_limit=16384*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/utils/model_dump/__init__.py#L458)

Get JSON-friendly information about a model.

The result is suitable for being saved as model_info.json,
or passed to burn_in_info.

Warning

`torch.utils.model_dump` is deprecated and unsafe on untrusted models:
inspecting a model can execute arbitrary code stored in it.