# get_default_qconfig_mapping

*class*torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping(*backend='x86'*, *version=0*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/ao/quantization/qconfig_mapping.py#L130)

Return the default QConfigMapping for post training quantization.

Parameters:

- **backend** (***) - the quantization backend for the default qconfig mapping, should be
one of ["x86" (default), "fbgemm", "qnnpack", "onednn"]
- **version** (***) - the version for the default qconfig mapping

Return type:

[*QConfigMapping*](torch.ao.quantization.qconfig_mapping.QConfigMapping.html#torch.ao.quantization.qconfig_mapping.QConfigMapping)