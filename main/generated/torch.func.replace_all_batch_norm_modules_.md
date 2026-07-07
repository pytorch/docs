# torch.func.replace_all_batch_norm_modules_

torch.func.replace_all_batch_norm_modules_(*root*)[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/_functorch/batch_norm_replacement.py#L16)

In place updates `root` by setting the `running_mean` and `running_var` to be None and
setting track_running_stats to be False for any nn.BatchNorm module in `root`

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)