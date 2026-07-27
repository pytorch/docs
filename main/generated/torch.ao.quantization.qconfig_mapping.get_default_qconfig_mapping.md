# get_default_qconfig_mapping

*class*torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping(*backend='x86'*, *version=0*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/ao/quantization/qconfig_mapping.py#L130)

Return the default QConfigMapping for post training quantization.

Parameters:

- **backend** (***) - the quantization backend for the default qconfig mapping, should be
one of ["x86" (default), "fbgemm", "qnnpack", "onednn"]
- **version** (***) - the version for the default qconfig mapping

Return type:

[*QConfigMapping*](torch.ao.quantization.qconfig_mapping.QConfigMapping.html#torch.ao.quantization.qconfig_mapping.QConfigMapping)