# get_default_qconfig_mapping

*class*torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping(*backend='x86'*, *version=0*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/ao/quantization/qconfig_mapping.py#L130)

Return the default QConfigMapping for post training quantization.

Parameters:

- **backend** (***) - the quantization backend for the default qconfig mapping, should be
one of ["x86" (default), "fbgemm", "qnnpack", "onednn"]
- **version** (***) - the version for the default qconfig mapping

Return type:

[*QConfigMapping*](torch.ao.quantization.qconfig_mapping.QConfigMapping.html#torch.ao.quantization.qconfig_mapping.QConfigMapping)