# torch.nn.functional.instance_norm

torch.nn.functional.instance_norm(*input*, *running_mean=None*, *running_var=None*, *weight=None*, *bias=None*, *use_input_stats=True*, *momentum=0.1*, *eps=1e-05*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/nn/functional.py#L2882)

Apply Instance Normalization independently for each channel in every data sample within a batch.

See [`InstanceNorm1d`](torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d), [`InstanceNorm2d`](torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d),
[`InstanceNorm3d`](torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)