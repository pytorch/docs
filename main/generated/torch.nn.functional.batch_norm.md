# torch.nn.functional.batch_norm

torch.nn.functional.batch_norm(*input*, *running_mean*, *running_var*, *weight=None*, *bias=None*, *training=False*, *momentum=0.1*, *eps=1e-05*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/nn/functional.py#L2865)

Apply Batch Normalization for each channel across a batch of data.

See [`BatchNorm1d`](torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d), [`BatchNorm2d`](torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d),
[`BatchNorm3d`](torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)