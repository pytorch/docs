# torch.utils.model_dump.get_model_info

torch.utils.model_dump.get_model_info(*path_or_file*, *title=None*, *extra_file_size_limit=16384*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/utils/model_dump/__init__.py#L458)

Get JSON-friendly information about a model.

The result is suitable for being saved as model_info.json,
or passed to burn_in_info.

Warning

`torch.utils.model_dump` is deprecated and unsafe on untrusted models:
inspecting a model can execute arbitrary code stored in it.