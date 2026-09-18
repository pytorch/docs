# torch.utils.model_dump.get_model_info

torch.utils.model_dump.get_model_info(*path_or_file*, *title=None*, *extra_file_size_limit=16384*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/utils/model_dump/__init__.py#L213)

Get JSON-friendly information about a model.

The result is suitable for being saved as model_info.json,
or passed to burn_in_info.