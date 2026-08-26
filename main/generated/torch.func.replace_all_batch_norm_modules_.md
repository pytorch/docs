# torch.func.replace_all_batch_norm_modules_

torch.func.replace_all_batch_norm_modules_(*root*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/_functorch/batch_norm_replacement.py#L16)

In place updates `root` by setting the `running_mean` and `running_var` to be None and
setting track_running_stats to be False for any nn.BatchNorm module in `root`

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)