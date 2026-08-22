# torch.onnx

## Overview

[Open Neural Network eXchange (ONNX)](https://onnx.ai/) is an open standard
format for representing machine learning models. The `torch.onnx` module captures the computation graph from a
native PyTorch [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module) model and converts it into an
[ONNX graph](https://github.com/onnx/onnx/blob/main/docs/IR.md).

The exported model can be consumed by any of the many
[runtimes that support ONNX](https://onnx.ai/supported-tools.html#deployModel), including
Microsoft's [ONNX Runtime](https://www.onnxruntime.ai).

Next example shows how to export a simple model.

```
import torch

class MyModel(torch.nn.Module):
 def __init__(self):
 super(MyModel, self).__init__()
 self.conv1 = torch.nn.Conv2d(1, 128, 5)

 def forward(self, x):
 return torch.relu(self.conv1(x))

input_tensor = torch.rand((1, 1, 128, 128), dtype=torch.float32)

model = MyModel()

torch.onnx.export(
 model, # model to export
 (input_tensor,), # inputs of the model,
 "my_model.onnx", # filename of the ONNX model
 input_names=["input"], # Rename inputs for the ONNX model
 dynamo=True # True or False to select the exporter to use
)
```

## torch.export-based ONNX Exporter

*The torch.export-based ONNX exporter is the newest exporter for PyTorch 2.6 and newer*

[torch.export](user_guide/torch_compiler/export.html#torch-export) engine is leveraged to produce a traced graph representing only the Tensor computation of the function in an
Ahead-of-Time (AOT) fashion. The resulting traced graph (1) produces normalized operators in the functional
ATen operator set (as well as any user-specified custom operators), (2) has eliminated all Python control
flow and data structures (with certain exceptions), and (3) records the set of shape constraints needed to
show that this normalization and control-flow elimination is sound for future inputs, before it is finally
translated into an ONNX graph.

[Learn more about the torch.export-based ONNX Exporter](onnx_export.html)

## Frequently Asked Questions

Q: I have exported my LLM model, but its input size seems to be fixed?

The tracer records the shapes of the example inputs. If the model should accept
inputs of dynamic shapes, set `dynamic_shapes` when calling [`torch.onnx.export()`](onnx_export.html#torch.onnx.export).

Q: How to export models containing loops?

See [torch.cond](higher_order_ops/cond.html#cond).

## Contributing / Developing

The ONNX exporter is a community project and we welcome contributions. We follow the
[PyTorch guidelines for contributions](https://github.com/pytorch/pytorch/blob/main/CONTRIBUTING.md), but you might
also be interested in reading our [development wiki](https://github.com/pytorch/pytorch/wiki/PyTorch-ONNX-exporter).

## torch.onnx APIs

### Functions

torch.onnx.export(*model*, *args=()*, *f=None*, ***, *kwargs=None*, *verbose=None*, *input_names=None*, *output_names=None*, *opset_version=None*, *dynamo=True*, *external_data=True*, *dynamic_shapes=None*, *custom_translation_table=None*, *report=False*, *optimize=True*, *verify=False*, *profile=False*, *dump_exported_program=False*, *artifacts_dir='.'*, *export_params=True*, *keep_initializers_as_inputs=False*, *dynamic_axes=None*, *training=<TrainingMode.EVAL: 0>*, *operator_export_type=<OperatorExportTypes.ONNX: 0>*, *do_constant_folding=True*, *custom_opsets=None*, *export_modules_as_functions=False*, *autograd_inlining=True*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/onnx/__init__.py#L65)

Exports a model into ONNX format.

Setting `dynamo=True` enables the new ONNX export logic
which is based on [`torch.export.ExportedProgram`](user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram) and a more modern
set of translation logic. This is the recommended and default way to export models
to ONNX.

When `dynamo=True`:

The exporter tries the following strategies to get an ExportedProgram for conversion to ONNX.

1. If the model is already an ExportedProgram, it will be used as-is.
2. Use [`torch.export.export()`](user_guide/torch_compiler/export/api_reference.html#torch.export.export) and set `strict=False`.
3. Use [`torch.export.export()`](user_guide/torch_compiler/export/api_reference.html#torch.export.export) and set `strict=True`.

Parameters:

- **model** ([*torch.nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)*|*[*torch.export.ExportedProgram*](user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram)*|**torch.jit.ScriptModule**|**torch.jit.ScriptFunction*) - The model to be exported.
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**,**...**]*) - Example positional inputs. Any non-Tensor arguments will be hard-coded into the
exported model; any Tensor arguments will become inputs of the exported model,
in the order they occur in the tuple.
- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*|**None*) - Path to the output ONNX model file. E.g. "model.onnx". This argument is kept for
backward compatibility. It is recommended to leave unspecified (None)
and use the returned [`torch.onnx.ONNXProgram`](onnx_export.html#torch.onnx.ONNXProgram) to serialize the model
to a file instead.
- **kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**|**None*) - Optional example keyword inputs.
- **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|**None*) - Whether to enable verbose logging.
- **input_names** (*Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - names to assign to the input nodes of the graph, in order.
- **output_names** (*Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - names to assign to the output nodes of the graph, in order.
These are labels only and do not affect the order of outputs. If the model
returns a dictionary, outputs are flattened in the dictionary's iteration
order regardless of the names specified here.
- **opset_version** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - The version of the
[default (ai.onnx) opset](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
to target. You should set `opset_version` according to the supported opset versions
of the runtime backend or compiler you want to run the exported model with.
Leave as default (`None`) to use the recommended version, or refer to
the ONNX operators documentation for more information.
- **dynamo** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to export the model with `torch.export` ExportedProgram instead of TorchScript.
- **external_data** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to save the model weights as an external data file.
This is required for models with large weights that exceed the ONNX file size limit (2GB).
When False, the weights are saved in the ONNX file with the model architecture.
- **dynamic_shapes** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**Any**,**...**]**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**Any**]**|**None*) - A dictionary or a tuple of dynamic shapes for the model inputs. Refer to
[`torch.export.export()`](user_guide/torch_compiler/export/api_reference.html#torch.export.export) for more details. This is only used (and preferred) when dynamo is True.
Note that dynamic_shapes is designed to be used when the model is exported with dynamo=True, while
dynamic_axes is used when dynamo=False.
- **custom_translation_table** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[**Callable**,**Callable**]**|**None*) - A dictionary of custom decompositions for operators in the model.
The dictionary should have the callable target in the fx Node as the key (e.g. `torch.ops.aten.stft.default`),
and the value should be a function that builds that graph using ONNX Script. This option
is only valid when dynamo is True.
- **report** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to generate a markdown report for the export process. This option
is only valid when dynamo is True.
- **optimize** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to optimize the exported model. This option
is only valid when dynamo is True. Default is True.
- **verify** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to verify the exported model using ONNX Runtime. This option
is only valid when dynamo is True.
- **profile** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to profile the export process. This option
is only valid when dynamo is True.
- **dump_exported_program** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to dump the [`torch.export.ExportedProgram`](user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram) to a file.
This is useful for debugging the exporter. This option is only valid when dynamo is True.
- **artifacts_dir** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)) - The directory to save the debugging artifacts like the report and the serialized
exported program. This option is only valid when dynamo is True.
- **export_params** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) -

**When ``f`` is specified**: If false, parameters (weights) will not be exported.

You can also leave it unspecified and use the returned [`torch.onnx.ONNXProgram`](onnx_export.html#torch.onnx.ONNXProgram)
to control how initializers are treated when serializing the model.
- **keep_initializers_as_inputs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) -

**When ``f`` is specified**: If True, all the
initializers (typically corresponding to model weights) in the
exported graph will also be added as inputs to the graph. If False,
then initializers are not added as inputs to the graph, and only
the user inputs are added as inputs.

Set this to True if you intend to supply model weights at runtime.
Set it to False if the weights are static to allow for better optimizations
(e.g. constant folding) by backends/runtimes.

You can also leave it unspecified and use the returned [`torch.onnx.ONNXProgram`](onnx_export.html#torch.onnx.ONNXProgram)
to control how initializers are treated when serializing the model.
- **dynamic_axes** (*Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Mapping**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]**|**Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Sequence**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]**|**None*) -

Deprecated: Prefer specifying `dynamic_shapes` when `dynamo=True`.

By default the exported model will have the shapes of all input and output tensors
set to exactly match those given in `args`. To specify axes of tensors as
dynamic (i.e. known only at run-time), set `dynamic_axes` to a dict with schema:

- KEY (str): an input or output name. Each name must also be provided in `input_names` or

`output_names`.
- VALUE (dict or list): If a dict, keys are axis indices and values are axis names. If a

list, each element is an axis index.

For example:

```
class SumModule(torch.nn.Module):
 def forward(self, x):
 return torch.sum(x, dim=1)

torch.onnx.export(
 SumModule(),
 (torch.ones(2, 2),),
 "onnx.pb",
 input_names=["x"],
 output_names=["sum"],
)
```

Produces:

```
input {
 name: "x"
 ...
 shape {
 dim {
 dim_value: 2 # axis 0
 }
 dim {
 dim_value: 2 # axis 1
...
output {
 name: "sum"
 ...
 shape {
 dim {
 dim_value: 2 # axis 0
...
```

While:

```
torch.onnx.export(
 SumModule(),
 (torch.ones(2, 2),),
 "onnx.pb",
 input_names=["x"],
 output_names=["sum"],
 dynamic_axes={
 # dict value: manually named axes
 "x": {0: "my_custom_axis_name"},
 # list value: automatic names
 "sum": [0],
 },
)
```

Produces:

```
input {
 name: "x"
 ...
 shape {
 dim {
 dim_param: "my_custom_axis_name" # axis 0
 }
 dim {
 dim_value: 2 # axis 1
...
output {
 name: "sum"
 ...
 shape {
 dim {
 dim_param: "sum_dynamic_axes_1" # axis 0
...
```
- **training** (*_C_onnx.TrainingMode*) - Deprecated option. Instead, set the training mode of the model before exporting.
- **operator_export_type** (*_C_onnx.OperatorExportTypes*) - Deprecated option. Only ONNX is supported.
- **do_constant_folding** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Deprecated option.
- **custom_opsets** (*Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**None*) - Deprecated option.
- **export_modules_as_functions** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|**Collection**[*[*type*](https://docs.python.org/3/library/functions.html#type)*[*[*torch.nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)*]**]*) - Deprecated option.
- **autograd_inlining** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Deprecated option.

Returns:

[`torch.onnx.ONNXProgram`](onnx_export.html#torch.onnx.ONNXProgram) if dynamo is True, otherwise None.

Return type:

[ONNXProgram](onnx_export.html#torch.onnx.ONNXProgram) | None

Changed in version 2.6: `training` is now deprecated. Instead, set the training mode of the model before exporting.
`operator_export_type` is now deprecated. Only ONNX is supported.
`do_constant_folding` is now deprecated. It is always enabled.
`export_modules_as_functions` is now deprecated.
`autograd_inlining` is now deprecated.

Changed in version 2.7: `optimize` is now True by default.

Changed in version 2.9: `dynamo` is now True by default.

Changed in version 2.11: `fallback` option has been removed.

torch.onnx.is_in_onnx_export()[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/onnx/__init__.py#L359)

Returns whether it is in the middle of ONNX export.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

### Classes

*class*torch.onnx.ONNXProgram(*model*, *exported_program*)

A class to represent an ONNX program that is callable with torch tensors.

Variables:

- **model** - The ONNX model as an ONNX IR model object.
- **exported_program** - The exported program that produced the ONNX model.

*class*torch.onnx.OnnxExporterError

Errors raised by the ONNX exporter. This is the base class for all exporter errors.

### Deprecated APIs

Deprecated since version 2.6: These functions are deprecated and will be removed in a future version.

torch.onnx.register_custom_op_symbolic(*symbolic_name*, *symbolic_fn*, *opset_version*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/onnx/_internal/torchscript_exporter/utils.py#L1842)

Registers a symbolic function for a custom operator.

When the user registers symbolic for custom/contrib ops,
it is highly recommended to add shape inference for that operator via setType API,
otherwise the exported graph may have incorrect shape inference in some extreme cases.
An example of setType is test_aten_embedding_2 in test_operators.py.

See "Custom Operators" in the module documentation for an example usage.

Parameters:

- **symbolic_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the custom operator in "<domain>::<op>"
format.
- **symbolic_fn** (*Callable*) - A function that takes in the ONNX graph and
the input arguments to the current operator, and returns new
operator nodes to add to the graph.
- **opset_version** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The ONNX opset version in which to register.

torch.onnx.unregister_custom_op_symbolic(*symbolic_name*, *opset_version*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/onnx/_internal/torchscript_exporter/utils.py#L1872)

Unregisters `symbolic_name`.

See "Custom Operators" in the module documentation for an example usage.

Parameters:

- **symbolic_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the custom operator in "<domain>::<op>"
format.
- **opset_version** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The ONNX opset version in which to unregister.

torch.onnx.select_model_mode_for_export(*model*, *mode*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/onnx/_internal/torchscript_exporter/utils.py#L91)

A context manager to temporarily set the training mode of `model`
to `mode`, resetting it when we exit the with-block.

Deprecated since version 2.7: Please set training mode before exporting the model.

Parameters:

- **model** - Same type and meaning as `model` arg to [`export()`](onnx_export.html#torch.onnx.export).
- **mode** (*TrainingMode*) - Same type and meaning as `training` arg to [`export()`](onnx_export.html#torch.onnx.export).