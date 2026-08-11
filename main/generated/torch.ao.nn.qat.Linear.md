# Linear

*class*torch.ao.nn.qat.Linear(*in_features*, *out_features*, *bias=True*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/qat/modules/linear.py#L16)

A linear module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Linear, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.Linear](https://pytorch.org/docs/stable/nn.html#torch.nn.Linear)
for documentation.

Similar to torch.nn.Linear, with FakeQuantize modules initialized to
default.

Variables:

**weight** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - fake quant module for weight

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/qat/modules/linear.py#L53)

Create a qat module from a float module or qparams_dict
Args: mod a float module, either produced by torch.ao.quantization utilities
or directly from user