# torch.onnx.verification

A set of tools to verify the correctness of ONNX models.

torch.onnx.verification.verify_onnx_program(*onnx_program*, *args=None*, *kwargs=None*, *compare_intermediates=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/onnx/_internal/exporter/_verification.py#L148)

Verify the ONNX model by comparing the values with the expected values from ExportedProgram.

Parameters:

- **onnx_program** (*_onnx_program.ONNXProgram*) - The ONNX program to verify.
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**,**...**]**|**None*) - The input arguments for the model.
- **kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**|**None*) - The keyword arguments for the model.
- **compare_intermediates** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to verify intermediate values. This is going
to take longer time, so it is disabled by default.

Returns:

VerificationInfo objects containing the verification information for each value.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[VerificationInfo]

*class*torch.onnx.verification.VerificationInfo(*name*, *max_abs_diff*, *max_rel_diff*, *abs_diff_hist*, *rel_diff_hist*, *expected_dtype*, *actual_dtype*)

Verification information for a value in the ONNX program.

This class contains the maximum absolute difference, maximum relative difference,
and histograms of absolute and relative differences between the expected and actual
values. It also includes the expected and actual data types.

The histograms are represented as tuples of tensors, where the first tensor is the
histogram counts and the second tensor is the bin edges.

Variables:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the value (output or intermediate).
- **max_abs_diff** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The maximum absolute difference between the expected and actual values.
- **max_rel_diff** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The maximum relative difference between the expected and actual values.
- **abs_diff_hist** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*torch.Tensor*](tensors.html#torch.Tensor)*,*[*torch.Tensor*](tensors.html#torch.Tensor)*]*) - A tuple of tensors representing the histogram of absolute differences.
The first tensor is the histogram counts and the second tensor is the bin edges.
- **rel_diff_hist** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*torch.Tensor*](tensors.html#torch.Tensor)*,*[*torch.Tensor*](tensors.html#torch.Tensor)*]*) - A tuple of tensors representing the histogram of relative differences.
The first tensor is the histogram counts and the second tensor is the bin edges.
- **expected_dtype** ([*torch.dtype*](tensor_attributes.html#torch.dtype)) - The data type of the expected value.
- **actual_dtype** ([*torch.dtype*](tensor_attributes.html#torch.dtype)) - The data type of the actual value.

asdict()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/onnx/_internal/exporter/_verification.py#L100)

Convert the VerificationInfo object to a dictionary.

Returns:

A dictionary representation of the VerificationInfo object.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

*classmethod*from_tensors(*name*, *expected*, *actual*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/onnx/_internal/exporter/_verification.py#L59)

Create a VerificationInfo object from two tensors.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the value.
- **expected** ([*Tensor*](tensors.html#torch.Tensor)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)) - The expected tensor.
- **actual** ([*Tensor*](tensors.html#torch.Tensor)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)) - The actual tensor.

Returns:

The VerificationInfo object.

Return type:

VerificationInfo