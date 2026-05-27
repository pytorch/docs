# torch.func.replace_all_batch_norm_modules_

torch.func.replace_all_batch_norm_modules_(*root*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/_functorch/batch_norm_replacement.py#L16)

In place updates `root` by setting the `running_mean` and `running_var` to be None and
setting track_running_stats to be False for any nn.BatchNorm module in `root`

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)