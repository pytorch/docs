# LinearBn1d

*class*torch.ao.nn.intrinsic.qat.modules.linear_fused.LinearBn1d(*in_features*, *out_features*, *bias=True*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/ao/nn/intrinsic/qat/modules/linear_fused.py#L16)

A LinearBn1d module is a module fused from Linear and BatchNorm1d, attached
with FakeQuantize modules for weight, used in quantization aware training.

We combined the interface of [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear) and
:class:torch.nn.BatchNorm1d`.

Similar to [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear), with FakeQuantize modules initialized
to default.

Variables:

- **freeze_bn** -
- **weight_fake_quant** - fake quant module for weight

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/ao/nn/intrinsic/qat/modules/linear_fused.py#L145)

Create a qat module from a float module or qparams_dict

Parameters:

**mod** - A float module, either produced by torch.ao.quantization
utilities or directly from the user.

train(*mode=True*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/ao/nn/intrinsic/qat/modules/linear_fused.py#L133)

Batchnorm's training behavior is using the self.training flag. Prevent
changing it if BN is frozen. This makes sure that calling model.train()
on a model with a frozen BN will behave properly.