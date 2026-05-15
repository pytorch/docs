# torch.export API Reference

torch.export.export(*mod*, *args*, *kwargs=None*, ***, *dynamic_shapes=None*, *strict=False*, *preserve_module_call_signature=()*, *prefer_deferred_runtime_asserts_over_guards=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/__init__.py#L59)

`export()` takes any nn.Module along with example inputs, and produces a traced graph representing
only the Tensor computation of the function in an Ahead-of-Time (AOT) fashion,
which can subsequently be executed with different inputs or serialized. The
traced graph (1) produces normalized operators in the functional ATen operator set
(as well as any user-specified custom operators), (2) has eliminated all Python control
flow and data structures (with certain exceptions), and (3) records the set of
shape constraints needed to show that this normalization and control-flow elimination
is sound for future inputs.

**Soundness Guarantee**

While tracing, `export()` takes note of shape-related assumptions
made by the user program and the underlying PyTorch operator kernels.
The output `ExportedProgram` is considered valid only when these
assumptions hold true.

Tracing makes assumptions on the shapes (not values) of input tensors.
Such assumptions must be validated at graph capture time for `export()`
to succeed. Specifically:

- Assumptions on static shapes of input tensors are automatically validated without additional effort.
- Assumptions on dynamic shape of input tensors require explicit specification
by using the `Dim()` API to construct dynamic dimensions and by associating
them with example inputs through the `dynamic_shapes` argument.

If any assumption can not be validated, a fatal error will be raised. When that happens,
the error message will include suggested fixes to the specification that are needed
to validate the assumptions. For example `export()` might suggest the
following fix to the definition of a dynamic dimension `dim0_x`, say appearing in the
shape associated with input `x`, that was previously defined as `Dim("dim0_x")`:

```
dim = Dim("dim0_x", max=5)
```

This example means the generated code requires dimension 0 of input `x` to be less
than or equal to 5 to be valid. You can inspect the suggested fixes to dynamic dimension
definitions and then copy them verbatim into your code without needing to change the
`dynamic_shapes` argument to your `export()` call.

Parameters:

- **mod** ([*Module*](../../../generated/torch.nn.Module.html#torch.nn.Module)) - We will trace the forward method of this module.
- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,**...**]*) - Example positional inputs.
- **kwargs** ([*Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Optional example keyword inputs.
- **dynamic_shapes** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,**...**]**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) -

An optional argument where the type should either be:
1) a dict from argument names of `f` to their dynamic shape specifications,
2) a tuple that specifies dynamic shape specifications for each input in original order.
If you are specifying dynamism on keyword args, you will need to pass them in the order that
is defined in the original function signature.

The dynamic shape of a tensor argument can be specified as either
(1) a dict from dynamic dimension indices to `Dim()` types, where it is
not required to include static dimension indices in this dict, but when they are,
they should be mapped to None; or (2) a tuple / list of `Dim()` types or None,
where the `Dim()` types correspond to dynamic dimensions, and static dimensions
are denoted by None. Arguments that are dicts or tuples / lists of tensors are
recursively specified by using mappings or sequences of contained specifications.
- **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - When disabled (default), the export function will trace the program through
Python runtime, which by itself will not validate some of the implicit assumptions
baked into the graph. It will still validate most critical assumptions like shape
safety. When enabled (by setting `strict=True`), the export function will trace
the program through TorchDynamo which will ensure the soundness of the resulting
graph. TorchDynamo has limited Python feature coverage, thus you may experience more
errors. Note that toggling this argument does not affect the resulting IR spec to be
different and the model will be serialized in the same way regardless of what value
is passed here.
- **preserve_module_call_signature** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**...**]*) - A list of submodule paths for which the original
calling conventions are preserved as metadata. The metadata will be used when calling
torch.export.unflatten to preserve the original calling conventions of modules.

Returns:

An `ExportedProgram` containing the traced callable.

Return type:

*ExportedProgram*

**Acceptable input/output types**

Acceptable types of inputs (for `args` and `kwargs`) and outputs include:

- Primitive types, i.e. `torch.Tensor`, `int`, `float`, `bool` and `str`.
- Dataclasses, but they must be registered by calling `register_dataclass()` first.
- (Nested) Data structures comprising of `dict`, `list`, `tuple`, `namedtuple` and
`OrderedDict` containing all above types.

*class*torch.export.ExportedProgram(*root*, *graph*, *graph_signature*, *state_dict*, *range_constraints*, *module_call_graph*, *example_inputs=None*, *constants=None*, ***, *verifiers=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1058)

Package of a program from `export()`. It contains
an [`torch.fx.Graph`](../../../fx.html#torch.fx.Graph) that represents Tensor computation, a state_dict containing
tensor values of all lifted parameters and buffers, and various metadata.

You can call an ExportedProgram like the original callable traced by
`export()` with the same calling convention.

To perform transformations on the graph, use `.module` property to access
an [`torch.fx.GraphModule`](../../../fx.html#torch.fx.GraphModule). You can then use
[FX transformation](https://pytorch.org/docs/stable/fx.html#writing-transformations)
to rewrite the graph. Afterwards, you can simply use `export()`
again to construct a correct ExportedProgram.

buffers()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1200)

Returns an iterator over original module buffers.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[*Tensor*](../../../tensors.html#torch.Tensor)]

*property*call_spec

Warning

This API is experimental and is *NOT* backward-compatible.

*property*constants

Warning

This API is experimental and is *NOT* backward-compatible.

*property*dialect*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Warning

This API is experimental and is *NOT* backward-compatible.

*property*example_inputs

Warning

This API is experimental and is *NOT* backward-compatible.

*property*graph

Warning

This API is experimental and is *NOT* backward-compatible.

*property*graph_module

Warning

This API is experimental and is *NOT* backward-compatible.

*property*graph_signature

Warning

This API is experimental and is *NOT* backward-compatible.

module(*check_guards=True*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1442)

Returns a self contained GraphModule with all the parameters/buffers inlined.

- When check_guards=True (default), a _guards_fn submodule is generated
and a call to a _guards_fn submodule is inserted right after placeholders
in the graph. This module checks guards on inputs.
- When check_guards=False, a subset of these checks are performed by a
forward pre-hook on the graph module. No _guards_fn submodule is generated.

Return type:

[*GraphModule*](../../../fx.html#torch.fx.GraphModule)

*property*module_call_graph

Warning

This API is experimental and is *NOT* backward-compatible.

named_buffers()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1208)

Returns an iterator over original module buffers, yielding
both the name of the buffer as well as the buffer itself.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Tensor*](../../../tensors.html#torch.Tensor)]]

named_parameters()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1191)

Returns an iterator over original module parameters, yielding
both the name of the parameter as well as the parameter itself.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Parameter*](../../../generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter)]]

parameters()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1183)

Returns an iterator over original module's parameters.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[*Parameter*](../../../generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter)]

*property*range_constraints

Warning

This API is experimental and is *NOT* backward-compatible.

run_decompositions(*decomp_table=None*, *decompose_custom_triton_ops=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1477)

Run a set of decompositions on the exported program and returns a new
exported program. By default we will run the Core ATen decompositions to
get operators in the
[Core ATen Operator Set](https://pytorch.org/docs/stable/torch.compiler_ir.html).

For now, we do not decompose joint graphs.

Parameters:

**decomp_table** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[**OperatorBase**,*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*]**|**None*) - An optional argument that specifies decomp behaviour for Aten ops
(1) If None, we decompose to core aten decompositions
(2) If empty, we don't decompose any operator

Return type:

*ExportedProgram*

Some examples:

If you don't want to decompose anything

```
ep = torch.export.export(model, ...)
ep = ep.run_decompositions(decomp_table={})
```

If you want to get a core aten operator set except for certain operator, you can do following:

```
ep = torch.export.export(model, ...)
decomp_table = torch.export.default_decompositions()
decomp_table[your_op] = your_custom_decomp
ep = ep.run_decompositions(decomp_table=decomp_table)
```

*property*state_dict

Warning

This API is experimental and is *NOT* backward-compatible.

*property*tensor_constants

Warning

This API is experimental and is *NOT* backward-compatible.

validate()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L1663)

Warning

This API is experimental and is *NOT* backward-compatible.

*property*verifier*: [Any](https://docs.python.org/3/library/typing.html#typing.Any)*

Warning

This API is experimental and is *NOT* backward-compatible.

*property*verifiers

Warning

This API is experimental and is *NOT* backward-compatible.

*class*torch.export.dynamic_shapes.AdditionalInputs[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L838)

Infers dynamic_shapes based on additional inputs.

This is useful particularly for deployment engineers who, on the one hand, may
have access to ample testing or profiling data that can provide a fair sense of
representative inputs for a model, but on the other hand, may not know enough
about the model to guess which input shapes should be dynamic.

Input shapes that are different than the original are considered dynamic; conversely,
those that are the same as the original are considered static. Moreover, we verify
that the additional inputs are valid for the exported program. This guarantees that
tracing with them instead of the original would have generated the same graph.

Example:

```
args0, kwargs0 = ... # example inputs for export

# other representative inputs that the exported program will run on
dynamic_shapes = torch.export.AdditionalInputs()
dynamic_shapes.add(args1, kwargs1)
...
dynamic_shapes.add(argsN, kwargsN)

torch.export(..., args0, kwargs0, dynamic_shapes=dynamic_shapes)
```

add(*args*, *kwargs=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L868)

Additional input `args()` and `kwargs()`.

dynamic_shapes(*m*, *args*, *kwargs=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L881)

Infers a `dynamic_shapes()` pytree structure by merging shapes of the
original input `args()` and `kwargs()` and of each additional input
args and kwargs.

verify(*ep*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L923)

Verifies that an exported program is valid for each additional input.

*class*torch.export.dynamic_shapes.Dim(*name*, ***, *min=None*, *max=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L109)

The `Dim` class allows users to specify dynamism in their exported
programs. By marking a dimension with a `Dim`, the compiler associates the
dimension with a symbolic integer containing a dynamic range.

The API can be used in 2 ways: Dim hints (i.e. automatic dynamic shapes:
`Dim.AUTO`, `Dim.DYNAMIC`, `Dim.STATIC`), or named Dims (i.e.
`Dim("name", min=1, max=2)`).

Dim hints provide the lowest barrier to exportability, with the user only
needing to specify if a dimension if dynamic, static, or left for the
compiler to decide (`Dim.AUTO`). The export process will automatically
infer the remaining constraints on min/max ranges and relationships between
dimensions.

Example:

```
class Foo(nn.Module):
 def forward(self, x, y):
 assert x.shape[0] == 4
 assert y.shape[0] >= 16
 return x @ y

x = torch.randn(4, 8)
y = torch.randn(8, 16)
dynamic_shapes = {
 "x": {0: Dim.AUTO, 1: Dim.AUTO},
 "y": {0: Dim.AUTO, 1: Dim.AUTO},
}
ep = torch.export(Foo(), (x, y), dynamic_shapes=dynamic_shapes)
```

Here, export would raise an exception if we replaced all uses of `Dim.AUTO` with `Dim.DYNAMIC`,
as `x.shape[0]` is constrained to be static by the model.

More complex relations between dimensions may also be codegened as runtime assertion nodes by the compiler,
e.g. `(x.shape[0] + y.shape[1]) % 4 == 0`, to be raised if runtime inputs do not satisfy such constraints.

You may also specify min-max bounds for Dim hints, e.g. `Dim.AUTO(min=16, max=32)`, `Dim.DYNAMIC(max=64)`,
with the compiler inferring the remaining constraints within the ranges. An exception will be raised if
the valid range is entirely outside the user-specified range.

Named Dims provide a stricter way of specifying dynamism, where exceptions are raised if the compiler
infers constraints that do not match the user specification. For example, exporting the previous
model, the user would need the following `dynamic_shapes` argument:

```
s0 = Dim("s0")
s1 = Dim("s1", min=16)
dynamic_shapes = {
 "x": {0: 4, 1: s0},
 "y": {0: s0, 1: s1},
}
ep = torch.export(Foo(), (x, y), dynamic_shapes=dynamic_shapes)
```

Named Dims also allow specification of relationships between dimensions, up
to univariate linear relations. For example, the following indicates one
dimension is a multiple of another plus 4:

```
s0 = Dim("s0")
s1 = 3 * s0 + 4
```

*class*torch.export.dynamic_shapes.ShapesCollection[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L741)

Builder for dynamic_shapes.
Used to assign dynamic shape specifications to tensors that appear in inputs.

This is useful particularly when `args()` is a nested input structure, and it's
easier to index the input tensors, than to replicate the structure of `args()` in
the `dynamic_shapes()` specification.

Example:

```
args = {"x": tensor_x, "others": [tensor_y, tensor_z]}

dim = torch.export.Dim(...)
dynamic_shapes = torch.export.ShapesCollection()
dynamic_shapes[tensor_x] = (dim, dim + 1, 8)
dynamic_shapes[tensor_y] = {0: dim * 2}
# This is equivalent to the following (now auto-generated):
# dynamic_shapes = {"x": (dim, dim + 1, 8), "others": [{0: dim * 2}, None]}

torch.export(..., args, dynamic_shapes=dynamic_shapes)
```

To specify dynamism for integers, we need to first wrap the integers using
_IntWrapper so that we have a "unique identification tag" for each integer.

Example:

```
args = {"x": tensor_x, "others": [int_x, int_y]}
# Wrap all ints with _IntWrapper
mapped_args = pytree.tree_map_only(int, lambda a: _IntWrapper(a), args)

dynamic_shapes = torch.export.ShapesCollection()
dynamic_shapes[tensor_x] = (dim, dim + 1, 8)
dynamic_shapes[mapped_args["others"][0]] = Dim.DYNAMIC

# This is equivalent to the following (now auto-generated):
# dynamic_shapes = {"x": (dim, dim + 1, 8), "others": [Dim.DYNAMIC, None]}

torch.export(..., args, dynamic_shapes=dynamic_shapes)
```

dynamic_shapes(*m*, *args*, *kwargs=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L812)

Generates the `dynamic_shapes()` pytree structure according to `args()` and `kwargs()`.

torch.export.dynamic_shapes.dims(**names*, *min=None*, *max=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L360)

Util to create multiple `Dim()` types.

Returns:

A tuple of `Dim()` types.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Dim*, ...]

torch.export.dynamic_shapes.refine_dynamic_shapes_from_suggested_fixes(*msg*, *dynamic_shapes*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/dynamic_shapes.py#L1281)

When exporting with `dynamic_shapes()`, export may fail with a ConstraintViolation error if the specification
doesn't match the constraints inferred from tracing the model. The error message may provide suggested fixes -
changes that can be made to `dynamic_shapes()` to export successfully.

Example ConstraintViolation error message:

```
Suggested fixes:

 dim = Dim('dim', min=3, max=6) # this just refines the dim's range
 dim = 4 # this specializes to a constant
 dy = dx + 1 # dy was specified as an independent dim, but is actually tied to dx with this relation
```

This is a helper function that takes the ConstraintViolation error message and the original `dynamic_shapes()` spec,
and returns a new `dynamic_shapes()` spec that incorporates the suggested fixes.

Example usage:

```
try:
 ep = export(mod, args, dynamic_shapes=dynamic_shapes)
except torch._dynamo.exc.UserError as exc:
 new_shapes = refine_dynamic_shapes_from_suggested_fixes(
 exc.msg, dynamic_shapes
 )
 ep = export(mod, args, dynamic_shapes=new_shapes)
```

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

torch.export.save(*ep*, *f*, ***, *extra_files=None*, *opset_version=None*, *pickle_protocol=2*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/__init__.py#L211)

Warning

Under active development, saved files may not be usable in newer versions
of PyTorch.

Saves an `ExportedProgram` to a file-like object. It can then be
loaded using the Python API `torch.export.load`.

Parameters:

- **ep** (*ExportedProgram*) - The exported program to save.
- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**IO**[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - implement write and flush) or a string containing a file name.
- **extra_files** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - Map from filename to contents
which will be stored as part of f.
- **opset_version** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - A map of opset names
to the version of this opset
- **pickle_protocol** ([*int*](https://docs.python.org/3/library/functions.html#int)) - can be specified to override the default protocol

Example:

```
import torch
import io

class MyModule(torch.nn.Module):
 def forward(self, x):
 return x + 10

ep = torch.export.export(MyModule(), (torch.randn(5),))

# Save to file
torch.export.save(ep, "exported_program.pt2")

# Save to io.BytesIO buffer
buffer = io.BytesIO()
torch.export.save(ep, buffer)

# Save with extra files
extra_files = {"foo.txt": b"bar".decode("utf-8")}
torch.export.save(ep, "exported_program.pt2", extra_files=extra_files)
```

torch.export.load(*f*, ***, *extra_files=None*, *expected_opset_version=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/__init__.py#L283)

Warning

Under active development, saved files may not be usable in newer versions
of PyTorch.

Warning

`torch.export.load()` uses pickle under the hood to load models. **Never load data from an untrusted source.**

Loads an `ExportedProgram` previously saved with
`torch.export.save`.

Parameters:

- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**IO**[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - A file-like object (has to
implement write and flush) or a string containing a file name.
- **extra_files** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - The extra filenames given in
this map would be loaded and their content would be stored in the
provided map.
- **expected_opset_version** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - A map of opset names
to expected opset versions

Returns:

An `ExportedProgram` object

Return type:

*ExportedProgram*

Example:

```
import torch
import io

# Load ExportedProgram from file
ep = torch.export.load("exported_program.pt2")

# Load ExportedProgram from io.BytesIO object
with open("exported_program.pt2", "rb") as f:
 buffer = io.BytesIO(f.read())
buffer.seek(0)
ep = torch.export.load(buffer)

# Load with extra files.
extra_files = {"foo.txt": ""} # values will be replaced with data
ep = torch.export.load("exported_program.pt2", extra_files=extra_files)
print(extra_files["foo.txt"])
print(ep(torch.randn(5)))
```

torch.export.pt2_archive._package.package_pt2(*f*, ***, *exported_programs=None*, *aoti_files=None*, *extra_files=None*, *opset_version=None*, *pickle_protocol=2*, *executorch_files=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L632)

Saves the artifacts to a PT2Archive format. The artifact can then be loaded
using `load_pt2`.

Parameters:

- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**IO**[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - A file-like object (has to
implement write and flush) or a string containing a file name.
- **exported_programs** (*Union**[**ExportedProgram**,*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**ExportedProgram**]**]*) - The exported program to save, or a dictionary mapping model name to an
exported program to save. The exported program will be saved under
models/*.json. If only one ExportedProgram is specified, this will
automatically be named "model".
- **aoti_files** (*Union**[*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**,*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]**]*) - A list of files
generated by AOTInductor via
`torch._inductor.aot_compile(..., {"aot_inductor.package": True})`,
or a dictionary mapping model name to its AOTInductor generated files.
If only one set of files is specified, this will automatically be named
"model".
- **extra_files** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**]*) - Map from filename to contents
which will be stored as part of the pt2.
- **opset_version** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - A map of opset names
to the version of this opset
- **pickle_protocol** ([*int*](https://docs.python.org/3/library/functions.html#int)) - can be specified to override the default protocol
- **executorch_files** (*Optional**[*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]**]*) - Optional executorch
artifacts to save.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [*IO*](https://docs.python.org/3/library/typing.html#typing.IO)[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)]

torch.export.pt2_archive._package.load_pt2(*f*, ***, *expected_opset_version=None*, *run_single_threaded=False*, *num_runners=1*, *device_index=-1*, *load_weights_from_disk=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L1059)

Loads all the artifacts previously saved with `package_pt2`.

Parameters:

- **f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**IO**[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - A file-like object (has to
implement write and flush) or a string containing a file name.
- **expected_opset_version** (*Optional**[**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - A map of opset names
to expected opset versions
- **num_runners** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of runners to load AOTInductor artifacts
- **run_single_threaded** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether the model should be run without
thread synchronization logic. This is useful to avoid conflicts with
CUDAGraphs.
- **device_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The index of the device to which the PT2 package is
to be loaded. By default, device_index=-1 is used, which corresponds
to the device cuda when using CUDA. Passing device_index=1 would
load the package to cuda:1, for example.

Returns:

A `PT2ArchiveContents` object which contains all the objects in the PT2.

Return type:

*PT2ArchiveContents*

torch.export.draft_export(*mod*, *args*, *kwargs=None*, ***, *dynamic_shapes=None*, *preserve_module_call_signature=()*, *strict=False*, *prefer_deferred_runtime_asserts_over_guards=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/__init__.py#L437)

A version of torch.export.export which is designed to consistently produce
an ExportedProgram, even if there are potential soundness issues, and to
generate a report listing the issues found.

Return type:

*ExportedProgram*

*class*torch.export.unflatten.FlatArgsAdapter[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L303)

Adapts input arguments with `input_spec` to align `target_spec`.

*abstract*adapt(*target_spec*, *input_spec*, *input_args*, *metadata=None*, *obj=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L308)

NOTE: This adapter may mutate given `input_args_with_path`.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

get_flat_arg_paths()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L320)

Returns a list of paths that are used to access the flat args.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

*class*torch.export.unflatten.InterpreterModule(*graph*, *ty=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L159)

A module that uses torch.fx.Interpreter to execute instead of the usual
codegen that GraphModule uses. This provides better stack trace information
and makes it easier to debug execution.

*class*torch.export.unflatten.InterpreterModuleDispatcher(*attrs*, *call_modules*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L254)

A module that carries a sequence of InterpreterModules corresponding to
a sequence of calls of that module. Each call to the module dispatches
to the next InterpreterModule, and wraps back around after the last.

torch.export.unflatten.unflatten(*module*, *flat_args_adapter=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/unflatten.py#L795)

Unflatten an ExportedProgram, producing a module with the same module
hierarchy as the original eager module. This can be useful if you are trying
to use `torch.export` with another system that expects a module
hierarchy instead of the flat graph that `torch.export` usually produces.

Note

The args/kwargs of unflattened modules will not necessarily match
the eager module, so doing a module swap (e.g. `self.submod =
new_mod`) will not necessarily work. If you need to swap a module out, you
need to set the `preserve_module_call_signature` parameter of
`torch.export.export()`.

Parameters:

- **module** (*ExportedProgram*) - The ExportedProgram to unflatten.
- **flat_args_adapter** (*Optional**[**FlatArgsAdapter**]*) - Adapt flat args if input TreeSpec does not match with exported module's.

Returns:

An instance of `UnflattenedModule`, which has the same module
hierarchy as the original eager module pre-export.

Return type:

*UnflattenedModule*

torch.export.register_dataclass(*cls*, ***, *serialized_type_name=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/__init__.py#L465)

Registers a dataclass as a valid input/output type for `torch.export.export()`.

Parameters:

- **cls** ([*type*](https://docs.python.org/3/library/functions.html#type)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) - the dataclass type to register
- **serialized_type_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - The serialized name for the dataclass. This is
- **this** (*required if you want to serialize the pytree TreeSpec containing*) -
- **dataclass.** -

Example:

```
import torch
from dataclasses import dataclass

@dataclass
class InputDataClass:
 feature: torch.Tensor
 bias: int

@dataclass
class OutputDataClass:
 res: torch.Tensor

torch.export.register_dataclass(InputDataClass)
torch.export.register_dataclass(OutputDataClass)

class Mod(torch.nn.Module):
 def forward(self, x: InputDataClass) -> OutputDataClass:
 res = x.feature + x.bias
 return OutputDataClass(res=res)

ep = torch.export.export(Mod(), (InputDataClass(torch.ones(2, 2), 1),))
print(ep)
```

*class*torch.export.decomp_utils.CustomDecompTable[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L31)

This is a custom dictionary that is specifically used for handling decomp_table in export.
The reason we need this is because in the new world, you can only *delete* an op from decomp
table to preserve it. This is problematic for custom ops because we don't know when the custom
op will actually be loaded to the dispatcher. As a result, we need to record the custom ops operations
until we really need to materialize it (which is when we run decomposition pass.)

Invariants we hold are:

1. All aten decomp is loaded at the init time
2. We materialize ALL ops when user ever reads from the table to make it more likely
that dispatcher picks up the custom op.
3. If it is write operation, we don't necessarily materialize
4. We load the final time during export, right before calling run_decompositions()

copy()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L104)

Return type:

*CustomDecompTable*

items()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L141)

keys()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L74)

materialize()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L145)

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*OperatorBase*, [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)]

pop(**args*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L111)

update(*other_dict*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/decomp_utils.py#L81)

torch.export.passes.move_to_device_pass(*ep*, *location*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/passes/__init__.py#L11)

Move the exported program to the given device.

Parameters:

- **ep** (*ExportedProgram*) - The exported program to move.
- **location** (*Union**[*[*torch.device*](../../../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) - The device to move the exported program to.
If a string, it is interpreted as a device name.
If a dict, it is interpreted as a mapping from
the existing device to the intended one

Returns:

The moved exported program.

Return type:

ExportedProgram

*class*torch.export.pt2_archive.PT2ArchiveReader(*archive_path_or_buffer*)

Context manager for reading a PT2 archive.

archive_version()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L226)

Get the archive version.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

get_file_names()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L239)

Get the file names in the archive.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

read_bytes(*name*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L211)

Read a bytes object from the archive.
name: The source file inside the archive.

Return type:

[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)

read_string(*name*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L218)

Read a string object from the archive.
name: The source file inside the archive.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

*class*torch.export.pt2_archive.PT2ArchiveWriter(*archive_path_or_buffer*)

Context manager for writing a PT2 archive.

close()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L185)

Close the archive.

count_prefix(*prefix*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L122)

Count the number of records that start with a given prefix.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

has_record(*name*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L116)

Check if a record exists in the archive.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

write_bytes(*name*, *data*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L132)

Write a bytes object to the archive.
name: The destination file inside the archive.
data: The bytes object to write.

write_file(*name*, *file_path*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L153)

Copy a file into the archive.
name: The destination file inside the archive.
file_path: The source file on disk.

write_folder(*archive_dir*, *folder_dir*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L166)

Copy a folder into the archive.
archive_dir: The destination folder inside the archive.
folder_dir: The source folder on disk.

write_string(*name*, *data*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L142)

Write a string object to the archive.
name: The destination file inside the archive.
data: The string object to write.

torch.export.pt2_archive.is_pt2_package(*serialized_model*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/pt2_archive/_package.py#L71)

Check if the serialized model is a PT2 Archive package.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch.export.exported_program.ModuleCallEntry(*fqn: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *signature: torch.export.exported_program.ModuleCallSignature | [None](https://docs.python.org/3/library/constants.html#None) = None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L114)

*class*torch.export.exported_program.ModuleCallSignature(*inputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[torch.export.graph_signature.TensorArgument | torch.export.graph_signature.SymIntArgument | torch.export.graph_signature.SymFloatArgument | torch.export.graph_signature.SymBoolArgument | torch.export.graph_signature.ConstantArgument | torch.export.graph_signature.CustomObjArgument | torch.export.graph_signature.TokenArgument]*, *outputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[torch.export.graph_signature.TensorArgument | torch.export.graph_signature.SymIntArgument | torch.export.graph_signature.SymFloatArgument | torch.export.graph_signature.SymBoolArgument | torch.export.graph_signature.ConstantArgument | torch.export.graph_signature.CustomObjArgument | torch.export.graph_signature.TokenArgument]*, *in_spec: torch.utils._pytree.TreeSpec*, *out_spec: torch.utils._pytree.TreeSpec*, *forward_arg_names: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L97)

torch.export.exported_program.default_decompositions()[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/exported_program.py#L322)

This is the default decomposition table which contains decomposition of
all ATEN operators to core aten opset. Use this API together with
`run_decompositions()`

Return type:

*CustomDecompTable*

*class*torch.export.custom_obj.ScriptObjectMeta(*constant_name*, *class_fqn*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/custom_obj.py#L7)

Metadata which is stored on nodes representing ScriptObjects.

*class*torch.export.graph_signature.ConstantArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *value: [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L64)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

value*: [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

*class*torch.export.graph_signature.CustomObjArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *class_fqn: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *fake_val: torch._library.fake_class_registry.FakeScriptObject | [None](https://docs.python.org/3/library/constants.html#None) = None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L57)

class_fqn*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

fake_val*: FakeScriptObject | [None](https://docs.python.org/3/library/constants.html#None)**= None*

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.ExportBackwardSignature(*gradients_to_parameters: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*, *gradients_to_user_inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*, *loss_output: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L158)

gradients_to_parameters*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

gradients_to_user_inputs*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

loss_output*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.ExportGraphSignature(*input_specs*, *output_specs*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L165)

`ExportGraphSignature` models the input/output signature of Export Graph,
which is a fx.Graph with stronger invariants guarantees.

Export Graph is functional and does not access "states" like parameters
or buffers within the graph via `getattr` nodes. Instead, `export()`
guarantees that parameters, buffers, and constant tensors are lifted out of
the graph as inputs. Similarly, any mutations to buffers are not included
in the graph either, instead the updated values of mutated buffers are
modeled as additional outputs of Export Graph.

The ordering of all inputs and outputs are:

```
Inputs = [*parameters_buffers_constant_tensors, *flattened_user_inputs]
Outputs = [*mutated_inputs, *flattened_user_outputs]
```

e.g. If following module is exported:

```
class CustomModule(nn.Module):
 def __init__(self) -> None:
 super(CustomModule, self).__init__()

 # Define a parameter
 self.my_parameter = nn.Parameter(torch.tensor(2.0))

 # Define two buffers
 self.register_buffer("my_buffer1", torch.tensor(3.0))
 self.register_buffer("my_buffer2", torch.tensor(4.0))

 def forward(self, x1, x2):
 # Use the parameter, buffers, and both inputs in the forward method
 output = (
 x1 + self.my_parameter
 ) * self.my_buffer1 + x2 * self.my_buffer2

 # Mutate one of the buffers (e.g., increment it by 1)
 self.my_buffer2.add_(1.0) # In-place addition

 return output

mod = CustomModule()
ep = torch.export.export(mod, (torch.tensor(1.0), torch.tensor(2.0)))
```

Resulting Graph is non-functional:

```
graph():
 %p_my_parameter : [num_users=1] = placeholder[target=p_my_parameter]
 %b_my_buffer1 : [num_users=1] = placeholder[target=b_my_buffer1]
 %b_my_buffer2 : [num_users=2] = placeholder[target=b_my_buffer2]
 %x1 : [num_users=1] = placeholder[target=x1]
 %x2 : [num_users=1] = placeholder[target=x2]
 %add : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%x1, %p_my_parameter), kwargs = {})
 %mul : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%add, %b_my_buffer1), kwargs = {})
 %mul_1 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%x2, %b_my_buffer2), kwargs = {})
 %add_1 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%mul, %mul_1), kwargs = {})
 %add_ : [num_users=0] = call_function[target=torch.ops.aten.add_.Tensor](args = (%b_my_buffer2, 1.0), kwargs = {})
 return (add_1,)
```

Resulting ExportGraphSignature of the non-functional Graph would be:

```
# inputs
p_my_parameter: PARAMETER target='my_parameter'
b_my_buffer1: BUFFER target='my_buffer1' persistent=True
b_my_buffer2: BUFFER target='my_buffer2' persistent=True
x1: USER_INPUT
x2: USER_INPUT

# outputs
add_1: USER_OUTPUT
```

To get a functional Graph, you can use `run_decompositions()`:

```
mod = CustomModule()
ep = torch.export.export(mod, (torch.tensor(1.0), torch.tensor(2.0)))
ep = ep.run_decompositions()
```

Resulting Graph is functional:

```
graph():
 %p_my_parameter : [num_users=1] = placeholder[target=p_my_parameter]
 %b_my_buffer1 : [num_users=1] = placeholder[target=b_my_buffer1]
 %b_my_buffer2 : [num_users=2] = placeholder[target=b_my_buffer2]
 %x1 : [num_users=1] = placeholder[target=x1]
 %x2 : [num_users=1] = placeholder[target=x2]
 %add : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%x1, %p_my_parameter), kwargs = {})
 %mul : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%add, %b_my_buffer1), kwargs = {})
 %mul_1 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%x2, %b_my_buffer2), kwargs = {})
 %add_1 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%mul, %mul_1), kwargs = {})
 %add_2 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%b_my_buffer2, 1.0), kwargs = {})
 return (add_2, add_1)
```

Resulting ExportGraphSignature of the functional Graph would be:

```
# inputs
p_my_parameter: PARAMETER target='my_parameter'
b_my_buffer1: BUFFER target='my_buffer1' persistent=True
b_my_buffer2: BUFFER target='my_buffer2' persistent=True
x1: USER_INPUT
x2: USER_INPUT

# outputs
add_2: BUFFER_MUTATION target='my_buffer2'
add_1: USER_OUTPUT
```

*property*assertion_dep_token*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[int](https://docs.python.org/3/library/functions.html#int), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)*

*property*backward_signature*: ExportBackwardSignature | [None](https://docs.python.org/3/library/constants.html#None)*

*property*buffers*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*buffers_to_mutate*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

get_replace_hook(*replace_inputs=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L568)

input_specs*: [list](https://docs.python.org/3/library/stdtypes.html#list)[InputSpec]*

*property*input_tokens*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*inputs_to_buffers*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*inputs_to_lifted_custom_objs*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*inputs_to_lifted_tensor_constants*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*inputs_to_parameters*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*lifted_custom_objs*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*lifted_tensor_constants*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*non_persistent_buffers*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

output_specs*: [list](https://docs.python.org/3/library/stdtypes.html#list)[OutputSpec]*

*property*output_tokens*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*parameters*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*parameters_to_mutate*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

replace_all_uses(*old*, *new*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L543)

Replace all uses of the old name with new name in the signature.

*property*user_inputs*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)]*

*property*user_inputs_to_mutate*: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

*property*user_outputs*: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)]*

*class*torch.export.graph_signature.InputKind(*value*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L81)

An enumeration.

BUFFER*= 3*

CONSTANT_TENSOR*= 4*

CUSTOM_OBJ*= 5*

PARAMETER*= 2*

TOKEN*= 6*

USER_INPUT*= 1*

*class*torch.export.graph_signature.InputSpec(*kind: torch.export.graph_signature.InputKind*, *arg: torch.export.graph_signature.TensorArgument | torch.export.graph_signature.SymIntArgument | torch.export.graph_signature.SymFloatArgument | torch.export.graph_signature.SymBoolArgument | torch.export.graph_signature.ConstantArgument | torch.export.graph_signature.CustomObjArgument | torch.export.graph_signature.TokenArgument*, *target: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*, *persistent: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L90)

arg*: TensorArgument | SymIntArgument | SymFloatArgument | SymBoolArgument | ConstantArgument | CustomObjArgument | TokenArgument*

kind*: InputKind*

persistent*: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)**= None*

target*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

*class*torch.export.graph_signature.OutputKind(*value*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L121)

An enumeration.

BUFFER_MUTATION*= 3*

GRADIENT_TO_PARAMETER*= 5*

GRADIENT_TO_USER_INPUT*= 6*

LOSS_OUTPUT*= 2*

PARAMETER_MUTATION*= 4*

TOKEN*= 8*

USER_INPUT_MUTATION*= 7*

USER_OUTPUT*= 1*

*class*torch.export.graph_signature.OutputSpec(*kind: torch.export.graph_signature.OutputKind*, *arg: torch.export.graph_signature.TensorArgument | torch.export.graph_signature.SymIntArgument | torch.export.graph_signature.SymFloatArgument | torch.export.graph_signature.SymBoolArgument | torch.export.graph_signature.ConstantArgument | torch.export.graph_signature.CustomObjArgument | torch.export.graph_signature.TokenArgument*, *target: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L132)

arg*: TensorArgument | SymIntArgument | SymFloatArgument | SymBoolArgument | ConstantArgument | CustomObjArgument | TokenArgument*

kind*: OutputKind*

target*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

*class*torch.export.graph_signature.SymBoolArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L52)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.SymFloatArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L47)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.SymIntArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L42)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.TensorArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L32)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

*class*torch.export.graph_signature.TokenArgument(*name: [str](https://docs.python.org/3/library/stdtypes.html#str)*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/export/graph_signature.py#L37)

name*: [str](https://docs.python.org/3/library/stdtypes.html#str)*