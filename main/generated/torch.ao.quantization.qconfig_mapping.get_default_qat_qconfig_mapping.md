# get_default_qat_qconfig_mapping

*class*torch.ao.quantization.qconfig_mapping.get_default_qat_qconfig_mapping(*backend='x86'*, *version=1*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/ao/quantization/qconfig_mapping.py#L143)

Return the default QConfigMapping for quantization aware training.

Parameters:

- **backend** (***) - the quantization backend for the default qconfig mapping, should be
one of ["x86" (default), "fbgemm", "qnnpack", "onednn"]
- **version** (***) - the version for the default qconfig mapping

Return type:

[*QConfigMapping*](torch.ao.quantization.qconfig_mapping.QConfigMapping.html#torch.ao.quantization.qconfig_mapping.QConfigMapping)