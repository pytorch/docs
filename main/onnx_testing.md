# torch.onnx.testing

Utilities to aid in testing exported ONNX models.

torch.onnx.testing.assert_onnx_program(*program*, ***, *rtol=None*, *atol=None*, *args=None*, *kwargs=None*, *strategy='TorchExportNonStrictStrategy'*, *backend='onnxruntime'*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/onnx/_internal/exporter/_testing.py#L18)

Assert that the ONNX model produces the same output as the PyTorch ExportedProgram.

Parameters:

- **program** (*_onnx_program.ONNXProgram*) - The `ONNXProgram` to verify.
- **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - Relative tolerance.
- **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - Absolute tolerance.
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**,**...**]**|**None*) - The positional arguments to pass to the program.
If None, the default example inputs in the ExportedProgram will be used.
- **kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**|**None*) - The keyword arguments to pass to the program.
If None, the default example inputs in the ExportedProgram will be used.
- **strategy** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - Assert the capture strategy used to export the program. Values can be
class names like "TorchExportNonStrictStrategy".
If None, the strategy is not asserted.
- **backend** (*Literal**[**'onnxruntime'**,**'reference'**]*) - The backend to use for evaluating the ONNX program.
Supported values are "onnxruntime" and "reference".