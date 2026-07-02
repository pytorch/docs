# torch.utils.model_dump.get_model_info

torch.utils.model_dump.get_model_info(*path_or_file*, *title=None*, *extra_file_size_limit=16384*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/utils/model_dump/__init__.py#L213)

Get JSON-friendly information about a model.

The result is suitable for being saved as model_info.json,
or passed to burn_in_info.